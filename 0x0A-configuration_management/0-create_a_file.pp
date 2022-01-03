# create a file in tmp directory

file {'school':
  ensure  => 'present',
  content => 'I love puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  path    => '/tmp/school',
}