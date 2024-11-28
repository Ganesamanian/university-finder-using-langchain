import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

google_api_key  = os.getenv("google_api_key")


# Create an instance of the LLM, using the 'gemini-pro' model with a specified creativity level
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.9)



def place_to_study(country, course):
    prompt_university = PromptTemplate(
                                input_variables = [country, course],
                                template = "Give me the college/university to study {course} in {country}. Give just college/university names as comma separated list"    
                                )
    # prompt_location = PromptTemplate(
    #                             input_variables = ['university_name'],
    #                             template = "Just Give one highlight of the {university_name}"    
    #                             )

    university_chain = LLMChain(llm = llm, prompt = prompt_university, output_key= 'university_name')
    # location_chain = LLMChain(llm = llm, prompt = prompt_location, output_key= 'location')
    main_chain = SequentialChain(chains = [university_chain],
                                 input_variables=['country', 'course'],
                                 output_variables = ['university_name'])
    
    return main_chain.invoke({'country': country, 'course': course})
    



if __name__ == "__main__":
    
    print(place_to_study("Germany", "Robotics"))