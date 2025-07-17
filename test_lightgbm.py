# test_lightgbm.py

import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer

def main():
    """
    Tests the LightGBM installation by training a simple classifier.
    """
    print("--- LightGBM Installation Test ---")

    try:
        # 1. Load a sample dataset from scikit-learn
        print("1. Loading breast cancer dataset...")
        data = load_breast_cancer()
        X, y = data.data, data.target
        print("   Dataset loaded successfully.")

        # 2. Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        print("2. Data split into training and testing sets.")

        # 3. Initialize and train the LightGBM Classifier
        # LightGBM is a high-performance gradient boosting framework [[1]].
        # We are using its scikit-learn compatible API for this test [[2]].
        print("3. Training LightGBM Classifier...")
        model = lgb.LGBMClassifier(objective="binary", verbosity=-1)
        model.fit(X_train, y_train)
        print("   Model training complete.")

        # 4. Make predictions and evaluate the model
        print("4. Evaluating model performance...")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"   Prediction accuracy: {accuracy:.4f}")

        print("\nSUCCESS: LightGBM is installed and working correctly!")

    except ImportError:
        print("\nERROR: Failed to import the 'lightgbm' library.")
        print("Please ensure the container was rebuilt after updating requirements.txt.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
