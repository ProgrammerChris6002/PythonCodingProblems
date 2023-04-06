def reverse_word (sentence) :
    words = sentence.split () # "split ()" method split's at whitespace by default
    words.reverse ()

    result = ' '.join (words)


    return result



reverse = input ('Enter your sentence: ')

print (reverse_word (reverse))




# Reverse Domain



def rev_domain (site) :
    parts = site.split ('.')
    parts.reverse ()

    rev = '.'.join (parts)
    return rev


site = 'www.programming-hero.com'

print (rev_domain (site))



# Code in one line


def rev_domain (site) :
    rev = '.'.join (reversed (site.split ('.')))
    return rev


site = 'www.programming-hero.com'
print (rev_domain (site))