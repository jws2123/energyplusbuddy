f = File.open("./Test_IDF.idf", "r")

i = 0
material_line = []
construction_line = []
property_list = []
space_break = []

f.each_line do |line|
  i += 1
  if line[0..7] == 'Material'
    material_line << i
    nextLine = f.gets
    while nextLine != "\r\n" do
      if nextLine.index('!')
        property_list << nextLine[nextLine.index('!')+3..nextLine.length-1]
      end
      nextLine = f.gets
      puts nextLine
    end
  elsif line[0..12] == 'Construction,'
    construction_line << i
    if line.index('!')
      property_list << line[line.index('!')+3..line.length-1]
    end
  end

  if line == "\r\n"
    space_break << i
  end

end

puts "% -------- Constructions -------- %"
construction_line.each do |j|
  line = File.readlines("Test_IDF.idf")
  commaInd = line[j].index(',') - 1 
  puts line[j][2..commaInd]
end

puts "% -------- Materials -------- %"
material_line.each do |j|
  line = File.readlines("Test_IDF.idf")
  commaInd = line[j].index(',') - 1 
  puts line[j][2..commaInd]
end

puts "% -------- Materials -------- %"
property_list.each do |p|
  puts p
end

f.close
