import openai
import os
def genimage(prompt):
    try:
        print("Somebody clicked generate image...so generating")
        print("generating image for " + prompt )
        #openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Image.create(prompt=prompt, n=1, size="256x256")
        print (str(response["data"][0]["url"]))
        return str(response["data"][0]["url"])
    except:
        return("https://static.wixstatic.com/media/c1a4c4_954c611181f34e1eb9a6ff00e4739862~mv2.png/v1/fill/w_290,h_197,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/MCM%20Moka%20(No%20Tagline).png")
    #print(response["data"][0]["url"]) blah blah blah