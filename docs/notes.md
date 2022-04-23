

To use the Cisco Meeting Server API you need to follow these steps:

    Connect via HTTPS via the same TCP ports as you would use to access the Web Admin Interface - which is typically 443.
    Enter your credentials to login to MMP.
    Configure a new 'api' user with a username and password, Set them using the MMP command user: add <username> (api).

This command creates a new api user and prompts for a password for the user which must be entered twice to ensure that the intended password is configured.

On first login, the user will be asked to configure a new password. You must provide these credentials in order to use the API.

Actions required

* need to look at init/set_up function to POST existing files to a CMS Server
*  create list_methods function
blq
* work out structure of class Session - how do we ctart to interact with CMS to get info and input info



https://ciscocms.docs.apiary.io/#introduction/general-structure-of-methods
https://developer.cisco.com/docs/cisco-meeting-server/#!getting-started-with-apis
https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Reference_Guides/Version-3-0/Cisco-Meeting-Server-API-Reference-Guide-3-0.pdf


https://sphinx-rtd-tutorial.readthedocs.io/en/latest/install.html


https://www.cisco.com/c/en/us/support/conferencing/meeting-server/series.html



/api/v1/accessQuery create new
/api/v1/callBrandingProfiles  
/api/v1/callBrandingProfiles/<id>
/api/v1/callBridgeGroups  
/api/v1/callBridgeGroups/<id>
/api/v1/callBridges  
/api/v1/callBridges/<id>
/api/v1/callLegProfiles  
/api/v1/callLegProfiles/<id>
/api/v1/callLegProfiles/<id>/usage
/api/v1/callLegs  
/api/v1/callLegs/<id>
/api/v1/callLegs/<id>/callLegProfileTrace
/api/v1/callLegs/<id>/cameraControl
/api/v1/callLegs/<id>/generateKeyframe
/api/v1/callProfiles  
/api/v1/callProfiles/<id>
/api/v1/calls  
/api/v1/calls/<id>
/api/v1/calls/<id>/callLegs
/api/v1/calls/<id>/callLegs/<id>
/api/v1/calls/<id>/diagnostics
/api/v1/calls/<id>/participants
/api/v1/calls/<id>/participants/*
/api/v1/compatibilityProfiles  
/api/v1/compatibilityProfiles/<id>
/api/v1/cospaceBulkParameterSets  
/api/v1/cospaceBulkParameterSets/<id>
/api/v1/cospaceBulkSyncs  
/api/v1/cospaceBulkSyncs/<id>
/api/v1/coSpaces  
/api/v1/coSpaces/<id>
/api/v1/coSpaces/<id>/accessMethods
/api/v1/coSpaces/<id>/accessMethods/<id>
/api/v1/coSpaces/<id>/coSpaceUsers
/api/v1/coSpaces/<id>/coSpaceUsers/<id>
/api/v1/coSpaces/<id>/diagnostics
/api/v1/coSpaces/<id>/meetingEntryDetail
/api/v1/coSpaces/<id>/messages
/api/v1/coSpaceTemplates  
/api/v1/coSpaceTemplates/<id>
/api/v1/coSpaceTemplates/<id>/accessMethodTemplates
/api/v1/coSpaceTemplates/<id>/accessMethodTemplates/<id>
/api/v1/dialTransforms  
/api/v1/dialTransforms/<id>
/api/v1/directorySearchLocations  
/api/v1/directorySearchLocations/<id>
/api/v1/dtmfProfiles  
/api/v1/dtmfProfiles/<id>
/api/v1/forwardingDialPlanRules  
/api/v1/forwardingDialPlanRules/<id>
/api/v1/inboundDialPlanRules  
/api/v1/inboundDialPlanRules/<id>
/api/v1/ivrBrandingProfiles  
/api/v1/ivrBrandingProfiles/<id>
/api/v1/ivrs  
/api/v1/ivrs/<id>
/api/v1/layoutTemplates  
/api/v1/layoutTemplates/<id>
/api/v1/layoutTemplates/<id>/template
/api/v1/ldapMappings  
/api/v1/ldapMappings/<id>
/api/v1/ldapServers  
/api/v1/ldapServers/<id>
/api/v1/ldapSources  
/api/v1/ldapSources/<id>
/api/v1/ldapSyncs  
/api/v1/ldapSyncs/<id>
/api/v1/ldapUserCoSpaceTemplateSources  
/api/v1/ldapUserCoSpaceTemplateSources/<id>
/api/v1/outboundDialPlanRules  
/api/v1/outboundDialPlanRules/<id>
/api/v1/participants  
/api/v1/participants/<id>
/api/v1/participants/<id>/callLegs
/api/v1/recorders  
/api/v1/recorders/<id>
/api/v1/recorders/<id>/status
/api/v1/streamers  
/api/v1/streamers/<id>
/api/v1/streamers/<id>/status
/api/v1/system/alarms  
/api/v1/system/cdrReceiver  
/api/v1/system/cdrReceivers  
/api/v1/system/cdrReceivers/<id>
/api/v1/system/configuration/cluster  
/api/v1/system/configuration/xmpp  
/api/v1/system/database  
/api/v1/system/diagnostics  
/api/v1/system/diagnostics/<id>
/api/v1/system/diagnostics/<id>/contents
/api/v1/system/licensing  
/api/v1/system/load  
/api/v1/system/multipartyLicensing  
/api/v1/system/multipartyLicensing/activePersonalLicenses  
/api/v1/system/profiles  
/api/v1/system/status  
/api/v1/tenantGroups  
/api/v1/tenantGroups/<id>
/api/v1/tenants  
/api/v1/tenants/<id>
/api/v1/turnServers  
/api/v1/turnServers/<id>
/api/v1/turnServers/<id>/status
/api/v1/uriUsageQuery create new
/api/v1/userProfiles  
/api/v1/userProfiles/<id>
/api/v1/users  
/api/v1/users/<id>
/api/v1/users/<id>/usercoSpaces
/api/v1/users/<id>/userCoSpaceTemplates
/api/v1/users/<id>/userCoSpaceTemplates/<id>
/api/v1/webBridges  
/api/v1/webBridges/<id>
/api/v1/webBridges/<id>/status
/api/v1/webBridges/<id>/updateCustomization

