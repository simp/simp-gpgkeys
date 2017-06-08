#!/usr/bin/rake -T

require 'simp/rake'

Simp::Rake::Pkg.new(File.dirname( __FILE__ ) )

keys = {
  'RPM-GPG-KEY-CentOS-6'          => 'Key fingerprint = C1DA C52D 1664 E8A4 386D  BA43 0946 FCA2 C105 B9DE',
  'RPM-GPG-KEY-CentOS-7'          => 'Key fingerprint = 6341 AB27 53D7 8A78 A7C2  7BB1 24C6 A8A7 F4A8 0EB5',
  'RPM-GPG-KEY-elasticsearch'     => 'Key fingerprint = 4609 5ACC 8548 582C 1A26  99A9 D27D 666C D88E 42B4',
  'RPM-GPG-KEY-EPEL-6'            => 'Key fingerprint = 8C3B E96A F230 9184 DA5C  0DAE 3B49 DF2A 0608 B895',
  'RPM-GPG-KEY-EPEL-7'            => 'Key fingerprint = 91E9 7D7C 4A5E 96F1 7F3E  888F 6A2F AEA2 352C 64E5',
  'RPM-GPG-KEY-fedora-25-primary' => 'Key fingerprint = C437 DCCD 558A 66A3 7D6F  4372 4089 D8F2 FDB1 9C98',
  'RPM-GPG-KEY-fedora-26-primary' => 'Key fingerprint = E641 850B 77DF 4353 78D1  D7E2 812A 6B4B 64DA B85D',
  'RPM-GPG-KEY-grafana'           => 'Key fingerprint = 4E40 DDF6 D76E 284A 4A67  80E4 8C8C 34C5 2409 8CB6',
  'RPM-GPG-KEY-grafana-legacy'    => 'Key fingerprint = 0C53 F985 09C5 1C6C FCB5  C4FC 30A3 D772 3DD1 8BDD',
  'RPM-GPG-KEY-PGDG-94'           => 'Key fingerprint = 68C9 E2B9 1A37 D136 FE74  D176 1F16 D2E1 442D F0F8',
  'RPM-GPG-KEY-puppet'            => 'Key fingerprint = 6F6B 1550 9CF8 E59E 6E46  9F32 7F43 8280 EF8D 349F',
  'RPM-GPG-KEY-puppetlabs'        => 'Key fingerprint = 47B3 20EB 4C7C 375A A9DA  E1A0 1054 B7A2 4BD6 EC30',
  'RPM-GPG-KEY-redhat-release'    => 'Key fingerprint = 567E 347A D004 4ADE 55BA  8A5F 199E 2F91 FD43 1D51',
  'RPM-GPG-KEY-SIMP'              => 'Key fingerprint = 103B 439D ADF4 AE61 FA69  98AF EE8C 77AF 7DA6 F216',
  'RPM-GPG-KEY-SIMP-6'            => 'Key fingerprint = F21E A54D 9C5A A9A5 AF7F  E002 1B5B 16A2 7667 220F',
}

task :fingerprint do
  keys.each do |key, fingerprint|
    unless `gpg --with-fingerprint GPGKEYS/#{key}` =~ /#{fingerprint}/
      fail("key #{key} doesn't match fingerprint #{fingerprint}")
    end
  end
end
