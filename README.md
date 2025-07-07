## Titanic Survivability Prediction App

This is a fully dockerized Flask-based ML app that predicts whether a Titanic passenger would survive based on user inputs like class, gender, age, number of siblings/spouses, parents/children aboard, and fare.

This project includes:

- A trained ML model
- CI/CD with GitHub Actions
- Dockerization
- Cloud deployment (GCP Compute Engine)
- Basic log monitoring

---

### Live App URL

[**https://titanic-ml-q8ua.onrender.com**](https://titanic-ml-q8ua.onrender.com)

---

## Features

- Logistic Regression and Random Forest models
- Logistic Regression Accuracy: 78.57%
- Random Forest Accuracy: 80.95%
- Visualizations (Survival by Sex, Survival by Class)
- User-friendly UI built with HTML/CSS
- Flask backend serving the trained ML model
- Dockerized for consistent deployment
- CI with linting and testing on push
- Deployed on GCP with a public IP
- Remote logs viewable via `docker logs` or Stackdriver (GCP Logging)

---

## Technologies Used

| Tool                | Purpose                        |
| ------------------- | ------------------------------ |
| Flask               | Web framework                  |
| scikit-learn        | ML model training              |
| Docker              | Containerization               |
| GitHub Actions      | CI for linting & testing       |
| GCP Compute Engine  | Cloud deployment               |
| GCP Logging Agent   | Monitoring logs                |
| Black / Flake8      | Python code formatting/linting |
| Pandas, NumPy       | Data preprocessing             |
| Seaborn, Matplotlib | Data visualization             |

---

## Project Structure

```
titanic-ml/
├── Dockerfile
├── README.md
├── app.py
├── data
│   └── titanic.csv
├── makefile
├── models
│   └── model.pkl
├── notebooks
│   ├── titanic_eda.ipynb
│   └── titanic_model.ipynb
├── requirements.txt
├── static
│   └── css
│       └── style.css
├── templates
│   ├── index.html
│   └── questions.html
└── tests
    └── test_app.py
```

---

## Setup Instructions

### Using Makefile

Ensure Docker is installed, then run:

```bash
make build     # Builds the Docker image with tag 'titanic-ml'
make run       # Runs the app on port 5050 (mapped to 5000 inside container)
make test      # Runs unit tests inside the container
make pathtest  # Runs pytest with PYTHONPATH set to project root
```

### Manual Docker Commands (e.g., for use on VMs like EC2 or GCP)

1. **Build the Docker image**

```bash
docker build -t titanic-ml .
```

2. **Run the Docker container**

```bash
docker run -d -p 80:5000 titanic-ml
```

This maps your app to the VM's port 80 (HTTP) so it can be accessed via public IP.

3. **Check logs**

```bash
docker logs <container_id>
```

4. **Pull from Docker Hub (if published)**

```bash
docker pull yourusername/titanic-ml
```

5. **Stop running containers**

```bash
docker ps         # list running containers
docker stop <id>  # stop container
```

---

## CI with GitHub Actions

Located in `.github/workflows/test.yml`

- Checks linting (black/flake8)
- Can be extended to run model or app tests

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install flake8 black
      - name: Lint with flake8
        run: flake8 .
```

---

## Sample Request & Output

**Form Inputs:**

- Pclass: 3
- Sex: Male
- Age: 22
- Siblings/Spouses: 1
- Parents/Children: 0
- Fare: 7.25

**Prediction Output:**

> Sorry, survival is unlikely.

---

## Resources Referenced

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Docker Docs](https://docs.docker.com/)
- [GCP Getting Started](https://cloud.google.com/gcp/get-started)
- [Stackdriver Logging](https://cloud.google.com/logging)

---

## Screenshots

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

---

## Credits

Built by **Labreo.**

