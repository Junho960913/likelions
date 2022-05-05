from googletrans import Translator

translator = Translator()
sentence = input('책을 읽으며 인상 깊었던 구절을 적어주세요: ')

result1 = translator.translate(sentence, dest="en")
result2 = translator.translate(sentence, dest="jp")
detect = translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detect.lang,":", result1.origin)
print(result1.dest,":", result1.text)
print(result2.dest,":", result2.text)
print("\n====================================\n")