gets
wall = [0, 0, 0] + gets.split(' ').map(&:to_i) + [0, 0, 0]
(3..wall.length - 4).each do |i|
    (-3..3).each do |j|
        if wall[i] - wall[i + j] > 4
            puts("False")
            exit
        end
    end
end
puts("True")
