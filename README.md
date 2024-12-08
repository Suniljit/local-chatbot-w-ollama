# Running a LLM Chatbot Locally Using Ollama and Langchain

## Set Up
1. Download and install Ollama from the link [here](https://ollama.com/). Ollama will be used to host the LLM models locally. 
2. Check that Ollama is installed correctly by running the following command:<br>
`ollama`
3. Download the model you want to run. In this case, we will use Llama3 8B. You can download the model using the following command:<br>
`ollama pull llama3`
4. Create a new conda environment.
5. Install the required packages by running the following command:<br>
   `pip install -r requirements.txt`


## Usage
1. Run the following code to start the chatbot:<br>
`python main.py`
2. To end the chat, type `exit` and press enter.