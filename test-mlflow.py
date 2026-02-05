"""Testing MLflow."""

# %%
# Initialisation

import logging
import tempfile
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import mlflow
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

mlflow.set_experiment("test")

rng = np.random.default_rng(42)

# %%
# Configure logger (to upload as a file to MLflow later)

log_file = Path("log.txt")
log_file.unlink(missing_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logging.captureWarnings(True)

# %%
# Processing

logging.info("Hello world!")

# Fake data
X = rng.standard_normal((100, 1))
y = 3 * X.squeeze() + 0.5 + rng.standard_normal(100) * 0.1
df = pd.DataFrame({"x": X.squeeze(), "y": y})

# Train model
model = LinearRegression()
model.fit(X, y)
preds = model.predict(X)
mse = mean_squared_error(y, preds)

# Plot
fig, ax = plt.subplots()
ax.scatter(X, y, label="data")
ax.plot(X, preds, color="red", label="model")
ax.set_title("Linear Fit")
ax.legend()

warnings.warn("This is a test warning!")

# %%
# Logging to MLflow

with mlflow.start_run():

    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("n_samples", len(X))

    mlflow.log_metric("mse", mse)

    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = Path(tmpdir) / "data.csv"
        df.to_csv(csv_path, index=False)
        mlflow.log_artifact(csv_path)

    mlflow.log_figure(fig, "fit.png")

    mlflow.log_artifact(log_file)

# %%
