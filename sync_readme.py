def synchronize_readme(original_file, translated_file):
    with open(original_file, 'r', encoding='utf-8') as orig:
        original_lines = orig.readlines()

    with open(translated_file, 'r', encoding='utf-8') as trans:
        translated_lines = trans.readlines()

    
    new_lines = [line for line in original_lines if line not in translated_lines]

    
    with open(translated_file, 'a', encoding='utf-8') as trans:
        for line in new_lines:
            trans.write(line)

if __name__ == "__main__":
    synchronize_readme('README.md', 'README.ua.md')
