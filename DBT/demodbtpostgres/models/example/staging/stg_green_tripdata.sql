with 

source as (
    select * from {{source('staging', 'green_taxi_data')}}
),

renamed as (
    select 
        "VendorId",
        lpep_pickup_datetime,
        lpep_dropoff_datetime,
        store_and_fwd_flag,
        RatecodeID,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        ehail_fee,
        improvement_surcharge,
        total_amount,
        payment_type,
        trip_type,
        congestion_surcharge

    from source
)

select * from renamed