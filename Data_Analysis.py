
# Speed/Response Time measurement 
import time

def generate_recommendations(user_input):
    # Simulate recommendation generation (Replace with actual logic)
    time.sleep(0.5)  # Simulating processing time
    return ["Song A", "Song B", "Song C"]

# Measure response time
start_time = time.time()
recommendations = generate_recommendations("User Playlist")
end_time = time.time()

response_time = end_time - start_time
print(f"Response Time: {response_time:.4f} seconds")


# Accuracy metrics (MRR, NDCG, Precision, Recall, F1-Score)
import numpy as np

def mean_reciprocal_rank(recommended_lists, relevant_items):
    """MRR implmentation"""
    reciprocal_ranks = []
    for recommended, relevant in zip(recommended_lists, relevant_items):
        for rank, item in enumerate(recommended, start=1):
            if item in relevant:
                reciprocal_ranks.append(1 / rank)
                break
        else:
            reciprocal_ranks.append(0)
    return np.mean(reciprocal_ranks)

# Example usage
recommended_lists = [["Song A", "Song B", "Song C"], ["Song D", "Song E", "Song F"]]
relevant_items = [["Song B"], ["Song D"]]

print("MRR:", mean_reciprocal_rank(recommended_lists, relevant_items))


def dcg_at_k(ranked_list, relevant_list, k):
    """NDCG implementation"""
    relevance_scores = [1 if song in relevant_list else 0 for song in ranked_list[:k]]
    return sum([rel / np.log2(i + 2) for i, rel in enumerate(relevance_scores)])

def ndcg_at_k(recommended_lists, relevant_items, k=5):
    ndcg_scores = []
    for recommended, relevant in zip(recommended_lists, relevant_items):
        ideal_dcg = dcg_at_k(relevant, relevant, k)
        actual_dcg = dcg_at_k(recommended, relevant, k)
        ndcg_scores.append(actual_dcg / ideal_dcg if ideal_dcg > 0 else 0)
    return np.mean(ndcg_scores)

# Example usage
print("NDCG:", ndcg_at_k(recommended_lists, relevant_items))


from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_precision_recall_f1(y_true, y_pred):
    """Precision, recall, F1"""
    precision = precision_score(y_true, y_pred, average='micro')
    recall = recall_score(y_true, y_pred, average='micro')
    f1 = f1_score(y_true, y_pred, average='micro')
    return precision, recall, f1

# Example usage
y_true = [1, 1, 0, 1, 0, 0, 1]  # Ground truth (1 = relevant, 0 = not relevant)
y_pred = [1, 0, 1, 1, 0, 0, 1]  # Predictions

precision, recall, f1 = evaluate_precision_recall_f1(y_true, y_pred)
print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {f1:.2f}")


# Scalability test
import random

def generate_large_dataset(size=1000000):
    return ["Song " + str(i) for i in range(size)]

def test_scalability(dataset_size):
    dataset = generate_large_dataset(dataset_size)
    user_history = random.sample(dataset, 500)  # Simulating 500 liked songs
    
    start_time = time.time()
    recommended = random.sample(dataset, 10)  # Simulating a recommendation function
    end_time = time.time()
    
    print(f"Dataset Size: {dataset_size}, Response Time: {end_time - start_time:.4f} seconds")

# Test with different dataset sizes
for size in [10000, 100000, 1000000]:
    test_scalability(size)



# Comparing with spotify api
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# client_id = "YOUR_SPOTIFY_CLIENT_ID"
# client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# def get_spotify_recommendations(seed_tracks):
#     return [track['name'] for track in sp.recommendations(seed_tracks=seed_tracks, limit=5)['tracks']]

# # Example usage
# spotify_recommendations = get_spotify_recommendations(["3n3Ppam7vgaVa1iaRUc9Lp"])  # Sample Track ID
# print("Spotify Recommendations:", spotify_recommendations)



# Visualization and reporting
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve

def plot_precision_recall(y_true, y_scores):
    precision, recall, _ = precision_recall_curve(y_true, y_scores)
    plt.plot(recall, precision, marker='.')
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve")
    plt.show()

# # Example usage
# y_scores = [0.9, 0.75, 0.6, 0.4, 0.2, 0.1]  # Model scores
# plot_precision_recall(y_true, y_scores)


import seaborn as sns
import pandas as pd

data = {"Song": ["A", "B", "C", "D"], "Plays": [50, 70, 20, 90], "Skips": [5, 10, 15, 2]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
sns.heatmap(df.set_index("Song"), annot=True, cmap="coolwarm")
plt.title("User Engagement (Plays vs. Skips)")
plt.show()