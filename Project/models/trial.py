import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# Example data (replace with your actual data)
undiacritized_sentences = ["محمد", "جمال", "علي"]
diacritized_sentences = ["مُحَمَّد", "جَمَال", "عَلِيّ"]

# Create character-level mappings
chars = sorted(set(''.join(undiacritized_sentences)))
char_to_idx = {char: idx + 1 for idx, char in enumerate(chars)}  # Assigning 0 for padding
idx_to_char = {idx: char for char, idx in char_to_idx.items()}

# Convert sentences to character indices
undiacritized_sequences = [[char_to_idx[char] for char in sentence] for sentence in undiacritized_sentences]
diacritized_sequences = [[char_to_idx[char] for char in sentence] for sentence in diacritized_sentences]

# Padding sequences
max_length = max(max(len(seq) for seq in undiacritized_sequences), max(len(seq) for seq in diacritized_sequences))
undiacritized_sequences = [torch.tensor(seq + [0] * (max_length - len(seq))) for seq in undiacritized_sequences]
diacritized_sequences = [torch.tensor(seq + [0] * (max_length - len(seq))) for seq in diacritized_sequences]

# Dataset and DataLoader
class DiacriticDataset(Dataset):
    def __init__(self, undiacritized, diacritized):
        self.undiacritized = undiacritized
        self.diacritized = diacritized

    def __len__(self):
        return len(self.undiacritized)

    def __getitem__(self, idx):
        return self.undiacritized[idx], self.diacritized[idx]

dataset = DiacriticDataset(undiacritized_sequences, diacritized_sequences)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Model architecture
class DiacriticPredictor(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(DiacriticPredictor, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, vocab_size)

    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        output = self.fc(lstm_out)
        return output

# Initializing model and optimizer
model = DiacriticPredictor(len(chars) + 1, 64, 64)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training the model
num_epochs = 10
for epoch in range(num_epochs):
    for undiacritized, diacritized in dataloader:
        optimizer.zero_grad()
        output = model(undiacritized)
        loss = criterion(output.permute(0, 2, 1), diacritized)  # CrossEntropyLoss expects (N, C, H) format
        loss.backward()
        optimizer.step()

# Example inference (predict diacritics for new undiacritized sentence)
new_sentence = "محمود"
new_sequence = torch.tensor([[char_to_idx[char] for char in new_sentence]])
padded_sequence = torch.nn.functional.pad(new_sequence, (0, max_length - len(new_sequence[0])))

predicted_sequence = model(padded_sequence)
predicted_diacritics = [idx_to_char[int(torch.argmax(pred))] for pred in predicted_sequence[0] if int(torch.argmax(pred)) != 0]

print("Predicted Diacritics:", ''.join(predicted_diacritics))