
project( FlatCTExecutor )

set( CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/../../../../../CMake ${PROJECT_SOURCE_DIR}/../../../../CMake )

include( Shared )
include( QtAutogen )
include( Nucline-Master )

find_package( Qt5Core ${QT_VERSION} EXACT REQUIRED CONFIG )
find_package( Qt5Widgets ${QT_VERSION} EXACT REQUIRED CONFIG )
find_package( Qt5Xml ${QT_VERSION} EXACT REQUIRED CONFIG )


find_mediso_package( FlatCTCommon ${Nucline-Master_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( FlatCTStateMachine ${Nucline-Master_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( FlatCTLib ${Nucline-Master_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( XRayLib ${Nucline-Master_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( Log ${MCP_SDK_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( MEvent ${MCP_SDK_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( DriverBase ${MMB_SDK_VERSION} EXACT REQUIRED CONFIG )
find_mediso_package( MDR ${MCP_SDK_VERSION} EXACT REQUIRED CONFIG )


add_library(	${PROJECT_NAME} SHARED
				${sourcefiles} )


target_link_libraries(	${PROJECT_NAME}
						PRIVATE FlatCTCommon
						PRIVATE FlatCTStateMachine
						PRIVATE FlatCTLib
						PRIVATE XRayLib
						PRIVATE MEvent
						PRIVATE Log
						PRIVATE DriverBase
						PRIVATE MDR
						PRIVATE Qt5::Core
						PRIVATE Qt5::Widgets
						PRIVATE Qt5::Xml
						)

include( VersionInfo )
include( Install )

set_target_properties ( ${PROJECT_NAME} PROPERTIES FOLDER Nucline/Equipment/FlatCT )
