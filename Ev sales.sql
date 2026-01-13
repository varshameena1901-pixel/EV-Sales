# Total EV sales
select sum(ev_sales_quantity) as total_sales 
from ev_sales;

#State wise sales 
select state,sum(ev_sales_quantity) as total_sales
from ev_sales
group by state 
order by total_sales DESC;

#year wise tread 
select year, sum(ev_sales_quantity) as total_sales
from ev_sales
group by year
order by year;

#vehicle category analysis
select vehicle_category,sum(ev_sales_quantity) as total_sales
from ev_sales
group by vehicle_category;

#top 5 state 
select state, sum(ev_sales_quantity) as sales
from ev_sales
group by state 
order by sales DESC
limit 5;


