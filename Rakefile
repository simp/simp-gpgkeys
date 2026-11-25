#!/usr/bin/rake -T

require 'simp/rake'
require 'yaml'
require 'open-uri'

Simp::Rake::Pkg.new(File.dirname( __FILE__ ) )

task :fingerprint do
  keys = YAML.load_file('gpgkeys.yaml')
  mismatched = keys.values.reject do |info|
    `gpg --show-keys --with-fingerprint GPGKEYS/#{info[:name]}`.include?(info[:fingerprint])
  end
  mismatched.each do |info|
    puts "key #{info[:name]} doesn't match fingerprint #{info[:fingerprint]}"
  end
  abort("#{mismatched.size} key(s) failed the fingerprint check") unless mismatched.empty?
end

task :download do
  %x( rm GPGKEYS/* )

  keys = YAML.load_file('gpgkeys.yaml')
  keys.each do |key,info|
    puts "Downloading #{info[:source_url]}"
    content = URI.open(info[:source_url]).read
    File.write("GPGKEYS/#{info[:name]}", content)
  end
end
