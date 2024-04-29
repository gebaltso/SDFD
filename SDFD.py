from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
import random
import csv
import time

# for selecting one random choice excluding a specified (used in combined races like [White:Black])
def choice_excluding(lst, exception):
    possible_choices = [v for v in lst if v != exception]
    return random.choice(possible_choices)

t = torch.rand(1000, 1000)
g = t.to("cuda")

# Define the output dierectory
output_dir = 'select_output_dir'

pipeline = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16, use_safetensors=True)
pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)
pipeline = pipeline.to("cuda")
images = []

#region prompt_options

gender = ['man, ', 'woman, ', 'boy, ', 'girl, ', 'baby boy, ', 'baby girl, ', 'androgynous person, ', 'gender fluid person, ', 'person having an androgynous appeal, ', 'person having male and female characteristics, ']
race = ['White, ', 'East Asian, ', 'Black, ', 'Pacific Islander, ', 'Indian, ', 'Southeast Asian, ', 'Middle Eastern, ', 'Latino, ']
moods = ['happy, ', 'sad, ', 'angry, ', 'tired, ', 'smiled, ', 'scared, ', 'excited, ', 'depressed, ', 'stressed, ']
hats = ['wearing cap, ', 'wearing hat, ', 'wearing pamela hat, ', 'wearing helmet, ', 'wearing headscarf, ', ' , ']
vision = ['wearing glasses, ', 'wearing sunglasses, ', 'wearing contact lenses, ', 'wearing colour contact lenses, ', ' , ']
vision2 = ['green eyes, ', 'blue eyes, ', 'brown eyes, ', 'black eyes, ']
acc = ['having wrinkles, ', ' , ']
hairColor = ['bald, ', 'black hair, ', 'blonde hair, ', 'brown hair, ', 'red hair, ', 'blue hair, ', 'green hair, ', 'pink hair, ', 'purple hair, ', 'white hair, ']
hairStyle = [ 'straight hair, ', 'curly hair, ', 'braid, ', 'ponytail, ', 'dreadlocks, ', 'hair clips, ', 'headband, ', 'short hair, ']
facePaints = ['wearing lipstick, ', 'wearing face blush, ', 'wearing rimmel, ', 'heavy make-up, ']
facial0 = ['wearing earrings, ']
facial1 = ['having piercing, ']
facial2 = ['having face tattoo, ']
facial3 = ['wearing medical mask, ']
facialAll = ['wearing earrings, ', 'having piercing, ', 'having face tattoo, ', 'wearing medical mask, ']
rel_muslimF = ['wearing hijab, ', 'wearing al-amira, ', 'wearing khimar, ', 'wearing chador, ', 'wearing niqab, ', 'wearing burqa, ']
rel_jewishF = ['wearing tichel, ', 'wearing snood, ']
rel_jewishM = ['wearing kippah, '] 
rel_hinduF = ['hindu ghoonghat, ']
rel_hinduM = ['hindu turban, ']
rel_crhristianF = ['nun hat, ', 'veil, ']
analysis = [' Ultra HD, ', ' 4K ', ' 8K ']
camera = [' Nikon Z9, ', 'Fujifilm XT3, ', 'Canon Eos 5D, ']
poses = ['front face, ', 'side profile, ', ' ,']
faceHair = ['mustache, ', 'beard, ', ', ']

#endregion

for i in range(10): # number of different prompts attempted

    g = random.choice(gender)
    r = random.choice(race)
    r2 = choice_excluding(race, r)
    races = '['+ r + ' ' + g + ' : ' + r2 + ' ' + g + '], '

    if g in {'man, ', 'woman, ', 'boy, ', 'girl, ', 'androgynous person, '}:
        gl = g[:2]
    elif g in {'baby boy, ', 'baby girl, '}:
        gl = g[0]+g[5]
    elif g == 'gender fluid person, ' :
        gl = 'gf'
    elif g == 'person having an androgynous appeal, ':
        gl = 'pa'
    else:
        gl = 'pc'

    rl = r[0]+r2[0]

    facial = [facial0, facial1, facial2, facial3, ' , ']
    facial_choice = random.choice(random.choices(facial, weights=map(len, facial))[0])

    if g == 'woman, ':  
        rel =  [rel_muslimF, rel_jewishF, rel_hinduF, rel_crhristianF, ' , ']
        rel_choice = random.choice(random.choices(rel, weights=map(len, rel))[0])
    elif g == 'man, ':
        rel =  [rel_jewishM, rel_hinduM, ' , ']
        rel_choice = random.choice(random.choices(rel, weights=map(len, rel))[0])
    else:
        rel =  [rel_muslimF, rel_jewishF, rel_hinduF, rel_crhristianF, rel_jewishM, rel_hinduM, ' , ']
        rel_choice = random.choice(random.choices(rel, weights=map(len, rel))[0])

    # Change the prompt accordingly to what we want to depict
    prompt = ( races + random.choice(hats) + random.choice(hairStyle)
              + random.choice(analysis) 
              + 'ultra realistic, textured skin, remarkable detailed pupils, realistic dull skin noise, visible skin detail, skin fuzz, dry skin, tone mapping, realistic background' )
    
    # number of images created with the same prompt
    num_images = 3
    
    start = time.time()
    images = pipeline(prompt = prompt, negative_prompt = 'bad anatomy, worst quality, unreal engine, animated, extra fingers, low resolution', num_images_per_prompt=num_images).images
    end = time.time()
    t = round(end-start, 2)
    for i, image in enumerate(images):
        image.save(f'{output_dir}/{gl+rl}-{str(i)}.jpg')
    
        with open('prompts.csv', 'a', newline='') as file:
            writer = csv.writer(file)   
            writer.writerow([f"{gl+rl}-{str(i)}", prompt, t])

torch.cuda.empty_cache()