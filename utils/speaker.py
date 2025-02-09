import re


def get_speaker_name(line):
    # Check for markdown format first
    markdown_match = re.match(r'^\*\*(.*?)\*\*:', line)
    if markdown_match:
        return markdown_match.group(1).strip()
    
    # Extract the speaker name before the colon for regular format
    speaker = line.split(':')[0].strip()
    
    # Helper function to split text into parts while preserving periods
    def split_into_parts(text):
        parts = []
        current = ''
        
        i = 0
        while i < len(text):
            if text[i].isspace():
                if current:
                    parts.append(current)
                    current = ''
            elif text[i] == '.':
                current += '.'
                if current:
                    parts.append(current)
                    current = ''
            else:
                current += text[i]
            i += 1
            
        if current:
            parts.append(current)
        return parts
    
    # Split the speaker name into parts
    parts = split_into_parts(speaker)
    
    if len(parts) > 0:
        # Process title if present
        start_idx = 0
        title = None
        
        # Check if first part is a title
        first_part = parts[0].lower()
        if first_part in ['dr', 'mr', 'mrs', 'ms']:
            title = parts[0] + '.'
            start_idx = 1
        elif first_part in ['dr.', 'mr.', 'mrs.', 'ms.']:
            title = parts[0]
            start_idx = 1
        
        # Process remaining parts
        result_parts = []
        if title:
            result_parts.append(title)
        
        # Handle single letter initial at start
        if start_idx < len(parts) and len(parts[start_idx]) == 1:
            result_parts.append(parts[start_idx])
            start_idx += 1
        
        i = start_idx
        while i < len(parts):
            current = parts[i]
            
            # Handle parts ending with period (initials)
            if current.endswith('.'):
                # If it's just a period, combine with previous part
                if current == '.':
                    if result_parts:
                        result_parts[-1] = result_parts[-1] + '.'
                else:
                    result_parts.append(current)
            else:
                # If next part is a period, combine them
                if i + 1 < len(parts) and parts[i + 1] == '.':
                    result_parts.append(current + '.')
                    i += 1
                else:
                    result_parts.append(current)
            i += 1
        
        return ' '.join(result_parts)
    
    return speaker





























def is_new_speaker(line):
    # Pattern to match speaker names, including markdown format
    pattern = r'^(?!Sub:|Fax:|Symbol:|Series:|Scrip|Subject:|MANAGEMENT:|MODERATOR:)((Dr\.|Mr\.|Mrs\.|Ms\.)?\s?)?([A-Z]\.?\s+)?((([A-Z]\.?)+[A-Z]?)|[A-Z][a-z]+)(\s?\.?\s?([A-Z](?:[a-z]+|\.?)))*:'
    markdown_pattern = r'^\*\*.*?\*\*:'
    return bool(re.match(pattern, line)) or bool(re.match(markdown_pattern, line))
