
Do you have any ideas to optimize the performance of your method   Reservaton.get_prev_reservation_id?

The initial version of the function looks like  this
```
    def get_prev_reservation_v2(self):
        last_reserved = Reservation.objects.select_related(rental=self.rental, id__lt=self.id)
        if last_reserved:
            return last_reserved[len(last_reserved) - 1].id
        return "--"

```

The sql  statement for this functions may perform similar operations to 
```
    select checkin, checkout rental from reservations 
    where rental = [self.rental from class] and id < [self.id from class]
```

This give rise to a few inefficiencies because I am fetching all reservatsions that occur before the current reservation even though I only need the preceeding one.


I can rework it and make it look as follows

```
   def get_prev_reservation_id(self):
        last_reserved = Reservation.objects.filter(rental=self.rental,id__lt=self.id).order_by("-id").only("id").first()
        return last_reserved.id if last_reserved else "--

```

The sql statement for this functions may perform similar operations to 
```
    select rental from reservations 
    where rental = [self.rental from class] and id < [self.id from class]
    order by [rental.id] desc
    limit 1
```

This only selects the rental field from the table after checking the reservatsions that occur before the current reservation but also orders them from highest to lowest and then limiting it to 1 item and picking the first item

Here is a quick mapping of what the addition chained functions do,

order_by("-id") -     order by [rental.id] desc
only("id") - select rental instead of  select checkin, checkout rental
first() - limit 1

This allows allow my db to do all the filtering operations as well as lowering the amount of data I read from the db.

I also cleaned up the if statement and put it in the return statement 