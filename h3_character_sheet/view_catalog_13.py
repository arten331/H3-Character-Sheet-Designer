"""H3 view order and camera conventions; no image or model dependencies."""
from .compiler import BODY_IDS, PRESETS as LEGACY_PRESETS, VIEW_IDS as LEGACY_VIEW_IDS

# Extended turnaround family: canonical three plus mirrored and three-quarter body views.
BODY_TURN_IDS = ('body_front', 'body_left', 'body_3q_left', 'body_right', 'body_3q_right', 'body_back')
BUST_IDS = ('bust_front',)
BODY_IDS = BODY_TURN_IDS

PORTRAIT_IDS = ('face_front', 'face_left', 'face_right', 'face_3q_left', 'face_3q_right', 'face_back')
CLOTHING_IDS = ('clothing_front', 'clothing_back')
# Extended turnaround: the three canonical body views plus mirrored/3q body angles
# and a dedicated bust (chest) detail view for consistent upper-body identity.
BODY_TURN_IDS = ('body_front', 'body_left', 'body_3q_left', 'body_right', 'body_3q_right', 'body_back')
BUST_IDS = ('bust_front',)
VIEW_IDS = (*PORTRAIT_IDS, *BODY_TURN_IDS, *BUST_IDS, *CLOTHING_IDS, 'hands', 'feet')
NATURAL_SURFACE = ('Preserve the character’s natural body surface, colors, markings and body structure from <Picture 1>. '
                   'Keep the visible torso and lower body free of garments. Retain compatible accessories.')
NATURAL_VIEW_PROMPTS = {
    'face_front': 'Front portrait with the complete head and upper chest.',
    'face_left': 'Profile portrait facing image-right, with the complete head and upper chest.',
    'face_right': 'Profile portrait facing image-left, with the complete head and upper chest.',
    'face_3q_left': 'Three-quarter portrait facing image-right, with the complete head and upper chest.',
    'face_3q_right': 'Three-quarter portrait facing image-left, with the complete head and upper chest.',
    'face_back': 'Portrait directly from behind, with the complete head and upper back.',
    'body_front': 'One complete front view in the character’s natural stance, including the entire silhouette.',
    'body_left': 'One complete profile facing image-right in the character’s natural stance, including the entire silhouette.',
    'body_3q_left': 'One three-quarter view angled toward image-right in the character’s natural stance, including the entire silhouette.',
    'body_right': 'One complete profile facing image-left in the character’s natural stance, including the entire silhouette.',
    'body_3q_right': 'One three-quarter view angled toward image-left in the character’s natural stance, including the entire silhouette.',
    'body_back': 'One complete view directly from behind in the character’s natural stance, including the entire silhouette.',
    'bust_front': 'One close-up of the chest and breasts from the front, cropped at the shoulders and below the ribcage.',
    'hands': 'One close-up of the character’s hands or forepaws as shown in the reference. Keep their shape and surface markings.',
    'feet': 'One close-up of the character’s feet or hind paws as shown in the reference. Keep their shape and surface markings.',
}
PRESETS = {**LEGACY_PRESETS,
           'head': PORTRAIT_IDS,
           'clothing': CLOTHING_IDS,
           'detail': VIEW_IDS,
           'turnaround6': BODY_TURN_IDS,
           'bust': BUST_IDS,
           'body9': (*BODY_TURN_IDS, *BUST_IDS, 'hands', 'feet')}
VIEW_DETAILS = {
    'face_front': ('front portrait', 'One front-facing bust, complete head and hair through the upper chest. Both eyes visible; no waist, legs or feet.'),
    'face_left': ('anatomical left-profile portrait', 'One strict anatomical left-profile bust, complete head and hair through the upper chest. The nose points to the RIGHT edge of the sheet, as in the H3 left-view convention. One visible eye; no front or three-quarter view.'),
    'face_right': ('anatomical right-profile portrait', 'One strict anatomical right-profile bust, complete head and hair through the upper chest. The nose points to the LEFT edge of the sheet. One visible eye; preserve asymmetric features rather than mirroring the person.'),
    'face_3q_left': ('anatomical left three-quarter portrait', 'One anatomical left three-quarter bust at 45 degrees, complete head and hair through the upper chest. The nose points toward the RIGHT edge. Both eyes visible with the farther eye foreshortened; not a front or strict profile view.'),
    'face_3q_right': ('anatomical right three-quarter portrait', 'One anatomical right three-quarter bust at 45 degrees, complete head and hair through the upper chest. The nose points toward the LEFT edge. Both eyes visible with the farther eye foreshortened; not a front or strict profile view.'),
    'face_back': ('rear portrait', 'One direct rear bust, complete back of head and hair through the upper chest. No face or eyes visible; do not turn the head.'),
    'body_front': ('full-body front', 'One full-body front view in a neutral standing pose. Include the complete head through both feet or footwear, with empty space above the head and beneath the soles.'),
    'body_left': ('full-body anatomical left profile', 'One strict anatomical left-profile full-body neutral standing view. Nose, chest and toes point to the RIGHT edge of the sheet. Include the complete head through feet or footwear; preserve asymmetric clothing.'),
    'body_3q_left': ('full-body left three-quarter', 'One full-body left three-quarter standing view at 45 degrees, chest angled toward the RIGHT edge of the sheet. Include the complete head through feet or footwear; both arms visible with the farther arm foreshortened.'),
    'body_right': ('full-body anatomical right profile', 'One strict anatomical right-profile full-body neutral standing view. Nose, chest and toes point to the LEFT edge of the sheet. Include the complete head through feet or footwear; preserve asymmetric features rather than mirroring the person.'),
    'body_3q_right': ('full-body right three-quarter', 'One full-body right three-quarter standing view at 45 degrees, chest angled toward the LEFT edge of the sheet. Include the complete head through feet or footwear; preserve asymmetric features rather than mirroring the person.'),
    'body_back': ('full-body back', 'One direct rear full-body neutral standing view. Include the complete head through feet or footwear. No face visible; do not turn the head.'),
    'bust_front': ('bust detail', 'One isolated chest close-up from the front of the same character, cropped at the shoulders and below the ribcage. Show the complete breasts and cleavage line only if naturally present; no head, arms below the shoulders, or legs. Preserve the reference skin tone, markings and body shape.'),
    'clothing_front': ('clothing front', 'One front-facing clothing detail of the same character wearing the outfit. Crop from the base of the neck to the complete lowest garment edge. Keep the head outside the frame and retain naturally visible arms and hands.'),
    'clothing_back': ('clothing back', 'One direct rear clothing detail of the same character wearing the outfit. Crop from the base of the neck to the complete lowest garment edge. Keep the head outside the frame and retain naturally visible arms and hands.'),
    'hands': ('hands detail', 'One isolated close-up of exactly two complete hands, one left and one right, cropped at the wrists. No head, torso or whole figure.'),
    'feet': ('feet and footwear detail', 'One isolated close-up of exactly one left and one right complete foot or footwear, including visible boot shafts. Show enclosing shoe surfaces as continuous material, with skin only through existing openings. No head, torso or whole figure.'),
}
