# Artist Recommender System: Personalizing Music Discovery

This repository contains the project **"Artist Recommender System: Personalizing Music Discovery"**, completed as part of the CPTS 440 Artificial Intelligence course. The goal of this project is to build a personalized music recommender system that helps users discover new artists using collaborative filtering. We experimented with matrix factorization via SVD and evaluated model performance using real user listening data from Last.fm.

---

## Project Description

### **Objective**
The aim of this project is to help users discover new music by recommending artists based on their listening behavior. We explored:
- Constructing a user-artist interaction matrix from Last.fm data.
- Applying collaborative filtering using the SVD algorithm.
- Evaluating model performance using RMSE and top-N recommendation accuracy.
- Addressing challenges such as data sparsity and the cold-start problem.

### **Key Features**
- **Data Preparation**: Cleaned and normalized the Last.fm dataset, filtering out low-activity users and artists.
- **Modeling**: Trained a collaborative filtering model using SVD to identify hidden patterns in user preferences.
- **Evaluation**: Used RMSE to measure prediction accuracy and displayed top-5 artist recommendations per user.
- **Challenges Addressed**: Cold start problem and sparse data matrix using matrix factorization.

---

## Deliverables

The following documents and materials summarize the project and its outcomes:

### 1. Project Proposal
- [Project Proposal (PDF)](docs/CPTS_440_Project_Proposal.pdf): Includes our initial proposal and ideas for the project.

### 2. Project Write-Up
- [Final Report (PDF)](docs/Artist_Recommender_System_Final_Report.pdf): Includes our thought process, problem formulation, solution overview, model implementation, evaluation metrics, and results.

### 3. Presentation Materials
- [Presentation Slides](docs/440_Presentation.pdf)

---

## Code and Demo

The code for the project is available in this repository. A demo notebook is also provided to guide you through model training and prediction.

### **Key Files**
- **Main Script**: [`Artist_recommendor.ipynb`](src/Artist_recommendor.ipynb) — trains the SVD model and outputs predictions.

### **Run the Demo**
1. **Clone this repository**:
```bash
   git clone https://github.com/your-org/artist-recommender.git
   cd artist-recommender
```

2. **Run the Notebook or Script**

- **`Artist_Recommender_Demo.ipynb`**: Walks through model training, evaluation, and generates top-5 artist recommendations per user.

Here is a link to a Google Colab where you can demo and learn how to run our code: [Link](https://colab.research.google.com/drive/1FEpDktGjCCizpCyoMowafp0hi-jR17Af?usp=sharing)

---

## Results and Insights

### **Evaluation Metrics**
- **RMSE on Test Set**: `0.0498` — indicates high predictive accuracy.
- **Cross-Validation (5-Fold)**: Consistently low RMSE across all folds.
- **Sample Output**: Top-5 personalized artist recommendations for users such as `jonocole`, `Knapster01`, `massdosage`, `Orlenay`, and `eartle`.

---

## Challenges

1. **Cold Start Problem**  
   Difficult to make recommendations for new users or artists without listening history.

2. **Sparse Data Matrix**  
   Many users interacted with only a few artists, limiting user-user or item-item overlap.

3. **Evaluation Limitations**  
   RMSE captures prediction error, but does not fully reflect recommendation quality or user satisfaction.

---

## Environment and Libraries

- **Environment**: Jupyter Notebook, Google Colab, Visual Studio Code  
- **Python Version**: 3.10  
- **Libraries Used**:
  - `surprise`
  - `pandas`
  - `numpy`
  - `matplotlib`

---

## Questions or Feedback

Feel free to reach out at [ethanvillalovoz.github.io](https://ethanvillalovoz.github.io)  
or submit an issue directly on this GitHub repository.
