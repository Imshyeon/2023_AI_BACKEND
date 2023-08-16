import locale # 현재 사용하는 시스템에서 등록된 OS의 지역값.
r=locale.getencoding()
print(r)
print(dir(locale))

print(locale.getdefaultlocale())
# lacale.getdefaultlocale() : DeprecationWarning: Use setlocale(), getencoding() and getlocale() instead
#('ko_KR', 'cp949')
# => locale.getdefaultlocale은 쓰지 마라.  DeprecationWarning 이거 나옴

print(locale.getlocale())
print(locale.getpreferredencoding())
print(locale.CHAR_MAX)
print(locale.localize('ko_KR'))


