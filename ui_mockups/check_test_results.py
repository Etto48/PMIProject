import matplotlib.pyplot as plt
import numpy as np

classes = 5
instances_per_class = np.random.randint(100, 1000, classes)
identity = np.identity(classes)
variation = np.random.rand(classes, classes) * 0.1
confusion_matrix = identity + variation
normalized_confusion_matrix = confusion_matrix / confusion_matrix.sum(axis=1, keepdims=True)
true_positives = np.diag(confusion_matrix)
false_positives = confusion_matrix.sum(axis=0) - true_positives
false_negatives = confusion_matrix.sum(axis=1) - true_positives
true_negatives = confusion_matrix.sum() - true_positives - false_positives - false_negatives
precisions = true_positives / (true_positives + false_positives)
precision = precisions @ instances_per_class / instances_per_class.sum()
recalls = true_positives / (true_positives + false_negatives)
recall = recalls @ instances_per_class / instances_per_class.sum()
f1 = 2 * precision * recall / (precision + recall)



fig, (data_ax, ax) = plt.subplots(1, 2)
fig.suptitle('Test Results')

ax.set_title('Confusion Matrix')
im = ax.imshow(normalized_confusion_matrix, cmap='Blues')
for i in range(classes):
    for j in range(classes):
        text = ax.text(
            j, 
            i, 
            round(normalized_confusion_matrix[i, j], 2),
            ha="center", 
            va="center", 
            color="black" if normalized_confusion_matrix[i, j] < 0.5 else "white")
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')

data_ax.set_title('Metrics')
data_ax.axis('off')
table = data_ax.table(
    cellText=[
        ['Metric', 'Value'],
        ['F1', f"{f1:.2%}"],
        ['Precision', f"{precision:.2%}"],
        ['Recall', f"{recall:.2%}"],
    ],
    cellLoc='center',
    loc='center',
)

plt.tight_layout()
plt.show()