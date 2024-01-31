from src import dbpedia_data_retriever, wikidata_data_retriever


def main():
    # extract_language_names()
    wikidata_data_retriever.get_data()
    # dbpedia_data_retriever.get_data()


if __name__ == '__main__':
    main()
