#!/ur/bin/env ruby
# Ruby script that accepts one argument
# Passes it to a regular expression matching method
puts ARGV[0].scan(/School/).join
