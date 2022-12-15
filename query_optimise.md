The code is not optimal for now as there are many SQL queries done during fetching the data in the view. Could you optimize it?

The current query is implemented as follow in the follow
```
   def get_prev_reservation_id(self):
        last_reserved = Reservation.objects.filter(rental=self.rental,id__lt=self.id).order_by("-id").only("id").first()
        return last_reserved.id if last_reserved else "--"

```

I reworked it as follows

```
    @classmethod
    def get_reservations(cls):
        previous_reservation_id = models.Subquery(
            Reservation.objects.filter(
                rental=models.OuterRef("rental"), id__lt=models.OuterRef("id")
            ).order_by("-id").values("id")[:1]
        )

        reservations = Reservation.objects.annotate(
            previous_reservation_id=previous_reservation_id

        )
        return reservations

```

Main changes are 


Instead of making one query in the view ( to fetch all resersevations) and one query with every reservation ( to check the id and get the previous reservation id). I do in one query that fetches all the reservations and uses a subquery to fetch the previous reservation id. 

Full query looks as follows (got this by printing out the reservations query in the models file)

```
SELECT 
    "reservations_reservation"."id", "reservations_reservation"."checkin",   "reservations_reservation"."checkout", "reservations_reservation"."rental_id", 
    (
        SELECT U0."id" 
        FROM 
            "reservations_reservation" U0 
            WHERE 
                (U0."id" < ("reservations_reservation"."id") AND U0."rental_id" = ("reservations_reservation"."rental_id")) 
            ORDER BY U0."id" DESC LIMIT 1) 
        AS 
    "previous_reservation_id" 
    FROM "reservations_reservation" ORDER BY "reservations_reservation"."rental_id" ASC
```

The main reason for using this approach is that all the filtering, sorting and labeling (annotation for previous_reservation_id for example) is done on the database side. 

Since the filtering occurs on the db side, I just have to call the function and assign it to a value and then pass it to jinja template, and then just get the r.previous_reservation_id in the view.

Another smaller change I made is having the view handle how the an empty previous_reservation_id is displayed. See code sample below

```
{% if r.previous_reservation_id %}
    <td>{{ r.previous_reservation_id }}</td>
{% else %}
    <td> -- </td>
{% endif %}
```

