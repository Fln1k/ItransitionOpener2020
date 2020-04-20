def h(a)
	a.reduce(Hash.new(0)){|h,e|h[e]+=1;h}
end

lines = Array.new
red = []
green = []
blue = []
File.open('guru99.txt').each { |line| lines << line.split(' ')}
line = lines[0]
counter = 0
while counter < line.length-1 do
	red << line[counter]
	green << line[counter+1]
	blue << line[counter+2]
	counter = counter+3
end
open('red.out', 'w') do |f|
	f.puts h(red)
end
open('green.out', 'w') do |f|
	f.puts h(green)
end
open('blue.out', 'w') do |f|
	f.puts h(blue)
end
