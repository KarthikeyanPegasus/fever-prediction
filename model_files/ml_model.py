


def fever_prediction(value,model):

    return model.predict(value)

if __name__ == "__main__":
    print(fever_prediction([[45,108]]))