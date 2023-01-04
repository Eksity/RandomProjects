import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    link = re.search(r"<iframe(?: .* ?)* src=\"https?://(?:www\.)?youtube\.com/embed/(.{11})\"(?: .* ?)*></iframe>",s)
    if link:
        extra = link.group(1)
        return f"https://youtu.be/{extra}"
    else:
        return "None"

if __name__ == "__main__":
    main()