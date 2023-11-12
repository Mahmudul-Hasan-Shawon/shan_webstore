template = """
<tr>
    <td>
        <div class="card text-start" style="
        width: 400px;
        height: 110px;">
            <div class="card-body d-flex">
                <div class="mr-2">
                    <img src="{icon_path}" class="logo" alt="" srcset="">
                </div>
                <div class="ps-3">
                    <h5 class="card-title">{app_name}</h5>
                    <p class="p-text">{description}</p>
                </div>
            </div>
        </div>
    </td>

    <td align="center">{platform}</td>
    <td align="center">
        <p>
            <a href="{website}" style="text-decoration: none">{website_display}</a>
        </p>
    </td>
    <td align="center">{version}</td>

    <td>
        <div class="row pt-2">
            <div class="col-md-6 offset-md-3">
                <div class="card-body d-flex justify-content-between">
                    <a href="{download_link}" download="" class="btn btn-sm text-white p-2" style="width: 200px;">Download
                        <span>&nbsp;</span>
                        <i class="fa-regular fa-circle-down"></i>
                    </a>
                </div>
            </div>
        </div>
    </td>
</tr>
"""

# User-input data
user_data = {
    "icon_path": "hello",
    "app_name": "SHELL",
    "description": "Powerful context menu manager for Windows File Explorer",
    "platform": "Windows",
    "website": "https://nilesoft.org/",
    "website_display": "nilesoft.org",
    "version": "1.9",
    "download_link": "https://nilesoft.org/download/shell/1.9/setup.exe"
}

# Format the template with user data
generated_html = template.format(**user_data)

# Print or use the generated HTML as needed
print(generated_html)

