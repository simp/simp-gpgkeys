#!/usr/bin/rake -T

require 'simp/rake'
require 'yaml'
require 'open-uri'

Simp::Rake::Pkg.new(File.dirname( __FILE__ ) )

task :fingerprint do
  keys = YAML.load_file('gpgkeys.yaml')
  keys.each do |key, info|
    fingerprint = info[:fingerprint]
    name = info[:name]
    unless `gpg --with-fingerprint GPGKEYS/#{info[:name]}` =~ /#{fingerprint}/
      puts "key #{info[:name]} doesn't match fingerprint #{fingerprint}"
    end
  end
end

task :download do
  keys = YAML.load_file('gpgkeys.yaml')
  keys.each do |key,info|
    # require 'pry';binding.pry
    content = open(info[:source_url]).read
    File.write("GPGKEYS/#{info[:name]}", content)
  end
end

