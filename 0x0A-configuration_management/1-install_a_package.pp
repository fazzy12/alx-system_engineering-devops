# Install Flask using pip3 with the specified version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}