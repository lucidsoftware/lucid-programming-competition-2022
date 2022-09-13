gets
code = gets.gsub('AB', '#')
a  = code.count('A')
b  = code.count('B')
ab = code.count('#')
c  = code.count('C')
score = (a * 1) + (b * 2) + (ab * 4) - (c * ab * ab)
puts(score)
