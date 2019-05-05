from scrapy.cmdline import execute


def main():

    try:
        execute(["scrapy", "crawl", "dangdang", "-a", "keyword=C#.net"])
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
