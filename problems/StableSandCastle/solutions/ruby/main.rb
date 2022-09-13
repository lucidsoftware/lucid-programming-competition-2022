gets
$wall = [0, 0, 0] + gets.split(' ').map(&:to_i) + [0, 0, 0]

def check(a, b)
    if $wall[a] - $wall[b] > 4
        puts("False")
        exit
    end
end

(3..$wall.length - 4).each do |i|
    (-3..3).each do |j|
        check(i, i + j)
    end
end

puts("True")
