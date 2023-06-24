from .http_type import HttpType

API_VERSION = "/api/v3"
API_PATH = {
    "login" :                               { "method": HttpType.POST     , "path": "/user/login"                            },
    "getPost" :                             { "method": HttpType.GET     , "path": "/post"                                  },
    "getCommunity" :                        { "method": HttpType.GET     , "path": "/community"                             },
    "listCommunities" :                     { "method": HttpType.GET     , "path": "/community/list"                        },
    "listPosts" :                           { "method": HttpType.GET     , "path": "/post/list"                             },
    "submitPost" :                          { "method": HttpType.POST    , "path": "/post"                                  },
    "editPost" :                            { "method": HttpType.PUT     , "path": "/post"                                  },
    "submitComment" :                       { "method": HttpType.POST    , "path": "/comment"                               },
    "likePost" :                            { "method": HttpType.POST    , "path": "/post/like"                             },
    "likeComment" :                         { "method": HttpType.POST    , "path": "/comment/like"                          },
    "followCommunity" :                     { "method": HttpType.POST    , "path": "/community/follow"                      },
    "resolveObject":                        { "method": HttpType.GET     , "path": "/resolve_object"                        },
    "search":                               { "method": HttpType.GET     , "path": "/search"                                },
    "getSite":                              { "method": HttpType.GET     , "path": "/site"                                  },
    "leaveAdmin":                           { "method": HttpType.POST    , "path": "/user/leave_admin"                      },
    "register":                             { "method": HttpType.POST    , "path": "/user/register"                         },
    "getPersonDetails":                     { "method": HttpType.GET     , "path": "/user"                                  },
    "getPersonMentions":                    { "method": HttpType.GET     , "path": "/user/mention"                          },
    "markPersonMentionAsRead":              { "method": HttpType.POST    , "path": "/user/mention/mark_as_read"             },
    "getReplies":                           { "method": HttpType.GET     , "path": "/user/replies"                          },
    "banPerson":                            { "method": HttpType.POST    , "path": "/user/ban"                              },
    "getBannedPersons":                     { "method": HttpType.GET     , "path": "/user/banned"                           },
    "blockUser":                            { "method": HttpType.POST    , "path": "/user/block"                            },
    "deleteAccount":                        { "method": HttpType.POST    , "path": "/user/delete_account"                   },
    "passwordReset":                        { "method": HttpType.POST    , "path": "/user/password_reset"                   },
    "passwordChangeAfterReset":             { "method": HttpType.POST    , "path": "/user/password_change"                  },
    "saveUserSettings":                     { "method": HttpType.PUT     , "path": "/user/save_user_settings"               },
    "markAllAsRead":                        { "method": HttpType.GET     , "path": "/user/mark_all_as_read"                 },
    "saveUserSettings":                     { "method": HttpType.PUT     , "path": "/user/save_user_settings"               },
    "changePassword":                       { "method": HttpType.PUT     , "path": "/user/change_password"                  },
    "getReportCount":                       { "method": HttpType.GET     , "path": "/user/report_count"                     },
    "getUnreadCount":                       { "method": HttpType.GET     , "path": "/user/unread_count"                     },
    "verifyEmail":                          { "method": HttpType.POST    , "path": "/user/verify_email"                     },
    "addAdmin":                             { "method": HttpType.POST    , "path": "/admin/add"                             },
    "getUnreadRegistrationApplicationCount":{ "method": HttpType.GET     , "path": "/admin/registration_application/count"  },
    "listRegistrationApplications":         { "method": HttpType.GET     , "path": "/admin/registration_application/list"   }
}
