# Changelog
Changelog for dupicolib

## [0.4.2] - 2024-08-18
### Added
- Added pin '0' to translation map for M3 to indicate a not connected pin

## [0.4.1] - 2024-08-15
### Added
- Support for OSC_DET command on the dupico

## [0.4.0] - 2024-08-12
### Changed
- Breaking change, added another layer of abstraction for board command classes, to allow easier virtual commands implementation

### Fixed
- Escaping in FW version check is fixed

## [0.3.2] - 2024-08-12
### Added
- Board pin remapping function can now ignore pins, if specified in their translation map, mapping them to negative values

## [0.3.1] - 2024-08-06
### Changed
- Reinitialize connection to the board (via DTR) only after the first failed connection attempt

## [0.3.0] - 2024-08-04
### Changed
- Make use of the binary protocol only
- Use DTR when retrying the connection to the board

### Removed
- Removed support for text based protocol

## [0.2.0] - 2024-07-29

### Added
- Support for multiple pin maps depending on model type
- Logging support during board connection
- Add code to parse and check fw firmware version
- Add support multiple command classes depending on hardware version and firmware

## [0.1.0] - 2024-07-26

- Initial release
