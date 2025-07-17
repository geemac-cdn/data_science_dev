# test_spark_xgboost.py

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from xgboost.spark import SparkXGBClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


def main():
    """
    Tests the XGBoost for Spark plugin.
    This version is configured to run in local mode for diagnostics.
    """
    print("--- XGBoost for Spark Test (Local Mode) ---")

    # 1. Create a SparkSession in local mode.
    print("1. Initializing SparkSession in local mode...")
    spark = (
        SparkSession.builder.appName("SparkXGBoostTest_Local")
        .config("spark.jars.packages", "ml.dmlc:xgboost4j-spark_2.12:2.0.3")
        .getOrCreate()
    )
    print("   SparkSession initialized successfully.")

    # 2. Create a sample Spark DataFrame.
    print("2. Creating a sample Spark DataFrame...")
    data = spark.createDataFrame([
        (1.0, 2.0, 0), (1.5, 2.5, 0), (5.0, 5.5, 1),
        (6.0, 5.0, 1), (1.2, 1.8, 0), (5.5, 5.2, 1)
    ], ["feature1", "feature2", "label"])

    # 3. Assemble features into a single vector column.
    print("3. Assembling feature vector...")
    # --- THIS IS THE CORRECTED LINE ---
    assembler = VectorAssembler(
        inputCols=["feature1", "feature2"], outputCol="features"
    )
    data = assembler.transform(data)

    # 4. Initialize and train the XGBoost Classifier.
    print("4. Training SparkXGBClassifier model...")
    xgb_classifier = SparkXGBClassifier(
        features_col="features",
        label_col="label"
    )
    model = xgb_classifier.fit(data)
    print("   Model training complete.")

    # 5. Make predictions and evaluate the model.
    print("5. Making predictions and evaluating...")
    predictions = model.transform(data)
    predictions.select("label", "prediction", "probability").show()

    evaluator = MulticlassClassificationEvaluator(
        labelCol="label", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print(f"   Prediction Accuracy: {accuracy:.4f}")

    print("\nSUCCESS: XGBoost for Spark is working correctly in local mode.")
    spark.stop()


if __name__ == "__main__":
    main()
