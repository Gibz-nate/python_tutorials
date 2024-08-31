def filter_messages(messages):
    filtered_messages = []
    counts = []

    for message in messages:
        words = message.split()
        filtered_message = []
        counter = 0

        for word in words:
            if word == "dang":
                counter += 1
            else:
                filtered_message.append(word)
        sentence = " ".join(filtered_message)
        filtered_messages.append(sentence)    
        counts.append(counter)    

    return filtered_messages, counts    
               


    
            
    
