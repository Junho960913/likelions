from googletrans import Translator

translator = Translator()
sentence = input('책을 읽으며 인상 깊었던 구절을 적어주세요: ')

result = translator.translate(sentence, dest="en")
detect = translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detect.lang,":", result.origin)
print(result.dest,":", result.text)
print("\n====================================\n")