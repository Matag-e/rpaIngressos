"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:

ModuleNotFoundError: No module named 'botcity'


This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    
    #if  bot.find_text( "NQA", threshold=230, waiting_time=10000):
    #    not_found("PSJ")
     
         
        
            
     
         
         

    while True:
        bot.page_down()
        if bot.find_text( "fazendinha", threshold=230, waiting_time=1000):
            if bot.find_text( "norte", threshold=230, waiting_time=1000):
                bot.click()  # Clique em "NORTE"
            if bot.find_text( "talita", threshold=230, waiting_time=10000):
                bot.click()  # Clique em "ROSANGELA"
                if bot.find_text( "regiane", threshold=230, waiting_time=10000):
                    bot.click()  # Clique em "CAIO"
                    if bot.find_text( "maylon", threshold=230, waiting_time=10000):
                        bot.click()  # Clique em "ANAB"
                        if bot.find_text( "kyara", threshold=230, waiting_time=10000):
                            bot.click()  # Clique em "CAIOL"
                            if bot.find_text( "murilo", threshold=230, waiting_time=10000):
                                bot.click()  # Clique em "TESTE"
                                if bot.find_text( "rhaje", threshold=230, waiting_time=10000):
                                    bot.click()  # Clique em "TESTE1"
                                    if bot.find_text( "continuar", threshold=230, waiting_time=10000):
                                        bot.click()  # Clique em "continuar"
                                        break
                                    else:
                                        bot.key_f5()  # Atualiza a página se "continuar" não for encontrado
                                else:
                                    bot.key_f5()  # Atualiza a página se "teste1" não for encontrado
                            else:
                                bot.key_f5()  # Atualiza a página se "teste" não for encontrado
                        else:
                            bot.key_f5()  # Atualiza a página se "caiol" não for encontrado
                    else:
                        bot.key_f5()  # Atualiza a página se "anab" não for encontrado
                else:
                    bot.key_f5()  # Atualiza a página se "caio" não for encontrado
            else:
                bot.key_f5()  # Atualiza a página se "rosangela" não for encontrado
        else:
            bot.key_f5()  # Atualiza a página se "norte" não for encontrado 
    
   








    #bot.click()
    
    
    
 


    

    # Implement here your logic...
    ...

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()