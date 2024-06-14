from openai import OpenAI

client= OpenAI(
    api_key= "put in your own API key!!!!"
)

print("Please enter the following prompts: \n1. An emotion \n2. A color \n3. A noun \n4. An adjective"+
      "\n5. A verb (past tense) \n6. A Plural noun \n7. A type of food \n8. Another adjective"+
      "\n9. A verb \n10. A noun (plural) \n11. An occupation \n12. A type of animal"+
      "\n13. An adjective \n14. A verb (past tense) \n15. A noun \n16. A name \n17. Another name \n")

#chatgpt accepts its inputs in strings
list_of_words= []
#to access the fist value you have to access the 0th value
string_of_words= ""
#a for loop starting from value 0, and ending before 17
#this loops runs 17 times, one for each catergory
#it will add each input to our list

for x in range(0,17):
    get_input= input("Enter a response to prompt #" + str(x+1) + ": ")
    list_of_words.append(get_input)

system_data= [
    {"role": "system", "content": "Generate a funny two-paragraph MadLib story using the words."},
    {"role":"user", "content": string_of_words.join(list_of_words)} #takes all words and put them together in a list, like making the story
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= system_data
)

#^^^^ pretty much evth is the same as the chatbot file

assistant_response= response.choices[0].message.content
system_data.append({"role": "assistant", "content": assistant_response})
print("Assistant: " + assistant_response)