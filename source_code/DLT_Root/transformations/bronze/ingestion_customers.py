import dlt

# Customer Expectations
customer_rules = {
    "rule_1" : "customer_id IS NOT NULL",
    "rule_2" : "customer_name IS NOT NULL"
}

# Ingesting customers
@dlt.table(
    name = "customers_stg"
)
@dlt.expect_all(customer_rules)
def customers_stg():
    df = spark.readStream.table("dlt.source.customers")
    return df