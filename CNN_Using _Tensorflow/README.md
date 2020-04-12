# CNN using Tensorflow
- Crawl dataset from OpenImages by tool: https://github.com/manhminno/OIDv4_ToolKit
- After crawling, resize the image to 32px to easily uploading to the Google Colab
- Model: Input->Conv(3, 3, 32), Act Relu, BatchNorm->Conv(3, 3, 32), Act Relu, BatchNorm, MaxPooling(2, 2)->Conv(3, 3, 64), Act Relu, BatchNorm->Conv(3, 3, 64), Act Relu, BatchNorm, MaxPooling(2, 2), Dropout(0.2)->Flatten()->Dense(512), Relu, BatchNorm, Dropout(0.5)->Densen(11), Softmax-> Output
- Training on Colab
