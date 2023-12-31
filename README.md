# Automatic Arabic Diacritization

## Overview

This project aims to automatically add diacritics (short vowel marks) to Arabic words using a Bi-LSTM (Bidirectional Long Short-Term Memory) model implemented with PyTorch. Diacritization is a crucial task in Arabic natural language processing (NLP), as it helps improve the accuracy of various applications such as text-to-speech synthesis, machine translation, and information retrieval.

## Table of Contents

- [Introduction](#automatic-arabic-diacritization)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/automatic-arabic-diacritization.git
   ```

2. Navigate to the project directory:

   ```bash
   cd automatic-arabic-diacritization
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To diacritize Arabic words using the trained model, use the provided inference script. Here's an example:

```bash
python diacritize.py --input "اللغة العربية جميلة"
```

Replace the input text with the Arabic words you want to diacritize.

## Data

The training data used for this project consists of a large corpus of Arabic text with manually annotated diacritics. You can find the dataset used for training in the `data` directory. If you want to use your own dataset, make sure it follows a similar format.

## Model Architecture

The diacritization model is based on a Bi-LSTM architecture implemented using PyTorch. The bidirectional nature of the LSTM helps capture contextual information from both past and future words, enhancing the model's ability to predict accurate diacritics.

## Training

To train the diacritization model, run the training script with your preferred configuration:

```bash
python train.py --epochs 10 --batch_size 64 --learning_rate 0.001
```

Adjust the hyperparameters as needed.

## Evaluation

Evaluate the model's performance on a separate test set using the evaluation script:

```bash
python evaluate.py --model_path models/best_model.pth --test_data data/test.txt
```

## Results

Our trained model achieved competitive results on the test set, demonstrating its effectiveness in adding diacritics to Arabic words accurately.

## Contributing

We welcome contributions from the community. If you find issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
