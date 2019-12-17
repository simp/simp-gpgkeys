# ------------------------------------------------------------------------------
# NOTE: SIMP Puppet rake tasks support ruby 2.4.5
# ------------------------------------------------------------------------------
gem_sources = ENV.fetch('GEM_SERVERS','https://rubygems.org').split(/[, ]+/)

gem_sources.each { |gem_source| source gem_source }

group :test do
  gem 'rake'
  gem 'rspec'
  gem 'metadata-json-lint'
  # Ruby code coverage
  gem 'simplecov'
  gem 'simp-rake-helpers', ENV.fetch('SIMP_RAKE_HELPERS_VERSION', ['>= 5.9', '< 6.0'])
end

group :development do
  gem 'pry'
  gem 'pry-doc'
end

group :system_tests do
  gem 'beaker'
  gem 'beaker-rspec'
  gem 'simp-beaker-helpers', ENV.fetch('SIMP_BEAKER_HELPERS_VERSION', ['>= 1.17', '< 2.0'])
end
