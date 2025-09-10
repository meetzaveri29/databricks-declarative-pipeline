import dlt

# Product Expectations
product_rules = {
    "rule_1" : "product_id is NOT NULL",
    "rule_2" : "price >= 0"
}

# Ingesting products
@dlt.table(
    name = "products_stg"
)
@dlt.expect_all(product_rules)
def products_stg():
    df = spark.readStream.table("dlt.source.products")
    return df