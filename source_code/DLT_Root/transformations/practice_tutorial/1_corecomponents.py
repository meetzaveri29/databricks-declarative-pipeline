# import dlt

# #Create streaming table
# @dlt.table(
#     name="first_stream_table"
# )
# def first_stream_table():
#     df = spark.readStream.table("dlt.source.orders")
#     return df

# #Create materialized view
# @dlt.table(
#     name= "first_mat_view"
# )
# def first_mat_view():
#     df = spark.read.table("dlt.source.orders")
#     return df

# #Create Batch view

# @dlt.view(
#     name = "first_batch_view"
# )
# def first_batch_view():
#     df = spark.read.table("dlt.source.orders")
#     return df

# #Create Streaming view

# @dlt.view(
#     name = "first_stream_view"
# )
# def first_stream_view():
#     df = spark.readStream.table("dlt.source.orders")
#     return df



